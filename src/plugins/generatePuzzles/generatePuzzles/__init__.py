"""
This is where the implementation of the plugin code goes.
The generatePuzzles-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('generatePuzzles')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class generatePuzzles(PluginBase):
  def main(self):
    
    import random
    
    active_node = self.active_node
    core = self.core
    logger = self.logger
    self.namespace = None
    META = self.META
    nodeHash = {}
    
    makeFirst = True
    makeSecond = True
    makeThird = True
    makeFourth = True
    makeFifth = True
    
    for node in core.load_sub_tree(active_node):
      nodeHash[core.get_path(node)] = node
      if core.get_attribute(node,'name') == 'FirstPuz':
        makeFirst = False
      if core.get_attribute(node,'name') == 'SecondPuz':
        makeSecond = False
      if core.get_attribute(node,'name') == 'ThirdPuz':
        makeThird = False
      if core.get_attribute(node,'name') == 'FourthPuz':
        makeFourth = False
      if core.get_attribute(node,'name') == 'FifthPuz': 
        makeFifth = False
      
    puzzles = []
    
    if makeFirst :
      puzz_one = core.copy_node(nodeHash['/f/V'], active_node)
      core.set_attribute(puzz_one, 'name', 'FirstPuz')
      core.set_attribute(puzz_one, 'target', random.randint(0,100))
      puzzles.append(puzz_one)
    if makeSecond :
      puzz_two = core.copy_node(nodeHash['/f/V'], active_node)
      core.set_attribute(puzz_two, 'name', 'SecondPuz')
      core.set_attribute(puzz_two, 'target', random.randint(0,100))
      puzzles.append(puzz_one)
    if makeThird :
      puzz_three = core.copy_node(nodeHash['/f/V'], active_node)
      core.set_attribute(puzz_three, 'name', 'ThirdPuz')
      core.set_attribute(puzz_three, 'target', random.randint(0,100))
      puzzles.append(puzz_three)
    if makeFourth :
      puzz_four = core.copy_node(nodeHash['/f/V'], active_node)
      core.set_attribute(puzz_four, 'name', 'FourthPuz')
      core.set_attribute(puzz_four, 'target', random.randint(0,100))
      puzzles.append(puzz_four)
    if makeFifth :
      puzz_five = core.copy_node(nodeHash['/f/V'], active_node)
      core.set_attribute(puzz_five, 'name', 'FifthPuz')
      core.set_attribute(puzz_five, 'target', random.randint(0,100))
      puzzles.append(puzz_five)
   
    for puzz in puzzles:
      oneHash = {}
      for node in core.load_sub_tree(puzz):
        oneHash[core.get_path(node)] = node 
      for childPath in core.get_children_paths(puzz):
        child = oneHash[childPath]
        if (core.is_instance_of(child, META["DIGIT"])): 
          core.set_attribute(child, 'value', random.randint(0,100))
        if (core.is_instance_of(child, META["Operation"])): 
          core.delete_node(child)

    self.util.save(root_node = core.get_root(active_node), commit_hash = self.commit_hash, branch_name = 'master')
