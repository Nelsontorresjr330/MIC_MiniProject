"""
This is where the implementation of the plugin code goes.
The checkValue-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('checkValue')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class checkValue(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
    self.namespace = None
    META = self.META
    nodeHash = {}
    for node in core.load_sub_tree(active_node):
      nodeHash[core.get_path(node)] = node 
    
    numbers = {}
    operations = {}
    dests = []
    
    for childPath in core.get_children_paths(active_node):
      child = nodeHash[childPath]
      if (core.is_instance_of(child, META["DIGIT"])): 
        num = core.get_attribute(child,"value")
        pos = core.get_attribute(child,"position")
        numbers[childPath] = [num,pos,child]
      if (core.is_instance_of(child, META["Operation"])): 
        op = core.get_attribute(child,"name")
        dest = nodeHash[core.get_pointer_path(child,"dst")]
        src = nodeHash[core.get_pointer_path(child,"src")]
        dests.append(nodeHash[core.get_pointer_path(child,"dst")]["nodePath"])
        op_node = child
        
        operations[op] = [op,src,dest,op_node]
      
    ops_in_order = {}
      
    #get first step
    for ops in operations.values():
      if ops[1]["nodePath"] not in dests:
        ops_in_order[0] = ops
        
    while len(ops_in_order) < len(operations):
      for ops in operations.values():
        if ops_in_order[len(ops_in_order)-1][2] == ops[1]:
          ops_in_order[len(ops_in_order)] = ops
      
    for ops in ops_in_order.values():
      for num in numbers:
        if num == ops[1]["nodePath"]:
          if ops[0] == 'Subtraction':
            numbers[ops[2]["nodePath"]][0] = numbers[ops[1]["nodePath"]][0] - numbers[ops[2]["nodePath"]][0]
            numbers[ops[1]["nodePath"]][0] = -1
          elif ops[0] == 'Addition':
            numbers[ops[2]["nodePath"]][0] = numbers[ops[1]["nodePath"]][0] + numbers[ops[2]["nodePath"]][0]
            numbers[ops[1]["nodePath"]][0] = -1
          elif ops[0] == 'Multiplication':
            numbers[ops[2]["nodePath"]][0] = numbers[ops[1]["nodePath"]][0] * numbers[ops[2]["nodePath"]][0]
            numbers[ops[1]["nodePath"]][0] = -1
          elif ops[0] == 'Division':
            numbers[ops[2]["nodePath"]][0] = numbers[ops[1]["nodePath"]][0] / numbers[ops[2]["nodePath"]][0]
            numbers[ops[1]["nodePath"]][0] = -1
          else:
            logger.info(ops[0] + 'does not exist')
     
    #Update the values    
    for num in numbers.values():
      core.set_attribute(num[2],'value',num[0])

    self.util.save(root_node = core.get_root(active_node), commit_hash = self.commit_hash, branch_name = 'master')


