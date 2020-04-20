#! /usr/bin/env python3

#packages needed
# matplotlib
# NetworkX
# PyGraphiz or Pydot

import Bio

from Bio import Phylo

#Bio.phylo

trees = Phylo.parse('phyloxml_examples.xml', 'phyloxml')
for tree in trees:
...     print(tree.name)


from cStringIO import StringIO

treedata = "(A, (B, C), (D, E))"
handle = StringIO(treedata)
tree = Phylo.read(handle, "newick")

#tree = Phylo.read(StringIO("(A, (B, C), (D, E))"), "newick")

tree1 = Phylo.read('example1.xml', 'phyloxml')
tree2 = Phylo.read('example2.xml', 'phyloxml')
Phylo.write([tree1, tree2], 'example-both.xml', 'phyloxml')

Phylo.convert('example.nhx', 'newick', 'example2.nex', 'nexus')

tree = Phylo.parse('phyloxml_examples.xml', 'phyloxml').next()
print(tree)
Phylogeny(description='phyloXML allows to use either a "branch_length"
attribute or element to indicate branch lengths.', name='example from
Prof. Joe Felsenstein s book "Inferring Phylogenies"')
    Clade()
        Clade(branch_length=0.06)
            Clade(branch_length=0.102, name='A')
            Clade(branch_length=0.23, name='B')
        Clade(branch_length=0.4, name='C')
...
<img src="Phylo-draw-apaf1.png" title="fig:Rooted phylogram, via Phylo.draw" alt="Rooted phylogram, via Phylo.draw" width="500" />

tree = Phylo.read('apaf.xml', 'phyloxml')
tree.ladderize()   # Flip branches so deeper clades are displayed at top
Phylo.draw(tree)

<img src="Phylo-apaf.png" title="Unrooted tree with colored nodes" alt="Unrooted tree with colored nodes" width="500" />

#for basic dendrogram
import pylab
tree = Phylo.read('apaf.xml', 'phyloxml')
Phylo.draw_graphviz(tree)
pylab.show()

#simple tree wiht defined branch lengths
tree = Phylo.parse('phyloxml_examples.xml', 'phyloxml').next()
Phylo.draw_ascii(tree)

apaf = Phylo.read('apaf.xml', 'phyloxml')
Phylo.draw_ascii(apaf)

#import networkx, pylab
#tree = Phylo.read('example.xml', 'phyloxml')
#net = Phylo.to_networkx(tree)
#networkx.draw(net)
#pylab.show()

Bio.Phylo.TreeConstruction #module
>>> from TreeConstruction import DistanceTreeConstructor
>>> constructor = DistanceTreeConstructor(calculator, 'nj')
>>> tree = constructor.build_tree(aln)
>>> print(tree)
Tree(rooted=False)
    Clade(branch_length=0, name='Inner3')
        Clade(branch_length=0.182692307692, name='Alpha')
        Clade(branch_length=0.0480769230769, name='Beta')
        Clade(branch_length=0.0480769230769, name='Inner2')
            Clade(branch_length=0.278846153846, name='Inner1')
                Clade(branch_length=0.0512820512821, name='Epsilon')
                Clade(branch_length=0.102564102564, name='Delta')
            Clade(branch_length=0.144230769231, name='Gamma')
```
