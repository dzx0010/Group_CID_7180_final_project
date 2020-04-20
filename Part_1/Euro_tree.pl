#!/usr/bin/env perl
use v5.16;     # sets strict and warnings
use Bio::Phylo::Forest;
use Bio::Phylo::Treedrawer;

my $string = '(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
(
MT328032.1:0.00000,
(
MT328033.1:0.00000,
MT328035.1:0.00000)
:0.00000)
:0.00018,
(
MT066156.1:0.00013,
MT093571.1:0.00014)
:0.00000)
:0.00000,
MT328034.1:0.00026)
:1.74974,
MT077125.1:1.75000)
:1.74781,
(
MT198651.1:0.00022,
MT198653.1:0.00020)
:0.00198)
:0.00198,
(
(
(
MT292569.1:0.00000,
MT292575.1:0.00000)
:0.00000,
(
MT292570.1:0.00000,
(
MT292580.1:0.00000,
MT233522.1:0.00000)
:0.00011)
:0.00000)
:0.00013,
MT292572.1:0.00010)
:0.00000)
:0.00017,
MT292573.1:0.00000)
:0.00000,
MT292574.1:0.00000)
:0.00000,
MT292578.1:0.00000)
:0.00000,
MT292571.1:0.00000)
:0.00000,
MT233523.1:0.00000)
:0.00000,
MT233519.1:0.00000)
:0.00000,
(
(
MT292577.1:0.00000,
(
MT256917.1:0.00023,
MT256918.1:0.00000)
:0.00000)
:0.00000,
MT198652.2:0.00000)
:0.00000)
:0.00000,
MT292576.1:0.00000)
:0.00000,
(
MT292579.1:0.00000,
MT292581.1:0.00000)
:0.00000)
:0.00000,
(
MT292582.1:0.00000,
MT233521.1:0.00000)
:0.00000,
MT233520.1:0.00000);';   

my $forest 
  = Bio::Phylo::IO->parse( -format => 'newick', -string => $string )->first;

my $treedrawer = Bio::Phylo::Treedrawer->new(
           -width  => 800,
           -height => 600,
           -shape  => 'CURVY', # curvogram
           -mode   => 'PHYLO', # phylogram
           -format => 'SVG'
);

$treedrawer->set_scale_options(
           -width => '100%',
           -major => '10%', # major cross hatch interval
           -minor => '2%',  # minor cross hatch interval
           -label => 'MYA',
);

$treedrawer->set_tree($forest);
$treedrawer->set_format('Svg');
print $treedrawer->draw;
