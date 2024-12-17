import sys
stdout = sys.stdout
# reload(sys)
sys.stdout = stdout


import pandas as pd

from graphviz import Digraph

from treelib import Tree
from queue import Queue

root_node = 'app_ordering_system_cal_sug_beijing'

sql = """with job_info as (
 select
  job_name
  ,max(job_owner) as job_owner
  ,avg(task_duration) as task_duration_avg
  ,max(department_name) as department_name
  ,avg(if_delayed_task) as delayed_rate_by_count
from
  data_smartorder.dm_copy_dwa_data_job_task_info_v1_da_view
where
  dt = '20231012'
group by job_name
)
 
 Select
    d.job_name,
    d.upstream_job_name,
    d.delay_condition,
    d.job_owner,
    d.job_business_line,
    i.task_duration_avg,
    i.department_name,
    i.delayed_rate_by_count
  from
    data_smartorder.dm_copy_dw_hive_meta_job_dependency_info_v1_di_view d
    left join job_info i on d.job_name = i.job_name 
  where
    dt = '20231017'
    and d.if_disabled = 'false'"""

columns = ['job_name', 'upstream_job_name', 'delay_condition',
           'job_owner', 'job_business_line', 'task_duration_avg',
           'department_name', 'delayed_rate_by_count']


def get_from_hive(sql, par=None):
    if par:
        sql = sql % par
    if sql.endswith(';'):
        pass
    else:
        sql = sql + ';'
    ss = """hive -e "%s" > dependencies.txt""" % (sql)
    #     print(ss)
    #     status, output = commands.getstatusoutput(ss)
    #     print(status)
    #     print(output)
    with open('/Users/pengtao.geng/Downloads/dependencies.txt') as fl:
        data = fl.readlines()
        #         print(data)
        mm = []
        for li in data:
            sl = li.split('\t')
            sl = map(lambda x: x.replace('\n', ''), sl)
            mm.append(sl)
    #         sln = pd.DataFrame(mm)
    return mm


def draw_tree(edges, info_dict):
    print
    "edges len = %d" % len(edges)
    edges_u = edges.drop_duplicates()
    print
    "edges_u len = %d" % len(edges_u)
    #     print edges_u

    g = Digraph('G', filename='dependence.gv')
    g.graph_attr['resolution'] = '480000'
    g.graph_attr['dpi'] = '220'
    for index, row in edges_u.iterrows():
        node_color = "black"
        edge_color = "black"
        lable = ""
        if info_dict.get(row[0]) is not None:
            lable = '\n'.join(info_dict.get(row[0]))
            if float(info_dict.get(row[0])[3]) > 30:
                node_color = "red"
            if float(info_dict.get(row[0])[4]) > 0.1:
                edge_color = "red"
        g.node(name=row[0], label=lable, color=node_color)
        g.edge(row[0], row[1], color=edge_color)

    g.view()


def build_job_dict(jobs):
    dict_edge = {}
    job_info_dict = {}
    for index, row in jobs.iterrows():
        l = list(dict_edge.setdefault(row[0], []))
        l.append(row[1])
        dict_edge[row[0]] = l

    return dict_edge


def build_job_info_dict(jobs):
    dict_edge = {}
    job_info_dict = {}
    for index, row in jobs.iterrows():
        job_info_dict[row[0]] = row[[0, 2, 3, 5, 7]]

    return job_info_dict


def build_jobs_df(mm):
    jobs = pd.DataFrame(mm, columns=columns)
    jobs['delayed_rate_by_count'] = jobs['delayed_rate_by_count'].map(lambda x: ("-1", x)[x != 'NULL']).map(
        lambda x: "{:.2f}".format(float(x)))
    jobs['task_duration_avg'] = jobs['task_duration_avg'].map(lambda x: ("-1", x)[x != 'NULL']).map(
        lambda x: "{:.2f}".format(float(x)))
    return jobs


def filter_jobs(jobs):
    tree = Tree()
    root = tree.create_node(root_node, root_node)
    edges_u = jobs.drop_duplicates()

    edge_dict = build_job_dict(edges_u)

    q = Queue(maxsize=0)
    q.put(root_node)

    while q.qsize() > 0:
        node = q.get()
        leafs = edge_dict.get(node)
        #     print "leafs :",leafs
        if leafs is None or len(leafs) <= 0:
            continue
        for leaf in leafs:
            if tree.get_node(leaf) is not None:
                continue
            q.put(leaf)
            tree.create_node(leaf, leaf, node, data=info_dict.get(leaf))

    #     for node in tree.all_nodes_itr():
    #         if node.tag.startswith('dw') or node.tag.startswith('ods') or node.tag.startswith('pdw'):
    #             if tree.contains(node.tag):
    #                 tree.remove_node(node.tag)

    #     for node in tree.children(root.identifier):
    #         q.put(node)
    #     while(q.qsize()>0):
    #         node=q.get()
    #         childs = tree.children(node.identifier)
    #         for child in childs:
    #             q.put(child)
    #         if info_dict.get(node.identifier) is not None:
    #             if float(info_dict.get(node.identifier)[3]) < 5:
    #                 for child in childs:
    #                     tree.move_node(child.identifier,tree.parent(node.identifier).identifier)
    #                 tree.remove_subtree(node.identifier)

    edges_tree = []
    for node in tree.all_nodes():
        if node.is_root():
            continue
        edges_tree.append([node.tag, node.bpointer])

    edges_tree_df = pd.DataFrame(edges_tree, columns=['node_e', 'node_s'])
    return edges_tree_df, tree


mm = get_from_hive(sql)
jobs = build_jobs_df(mm)
info_dict = build_job_info_dict(jobs)
jobs_need_df, tree = filter_jobs(jobs)
draw_tree(jobs_need_df, info_dict)
