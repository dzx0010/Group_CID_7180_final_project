#!/usr/bin/env python3
import sys
import getopt
import string
import os
import re
import glob

names = [];
scores = [];
active = []; ##only for UPGMA


########################################################################################################
########################################################################################################
###usage statement
########################################################################################################
########################################################################################################
def usage():
    print("This is Devan Bicher's Sequence Alignment Program for CSE 308, Project2");
    print("");
    print("The formatting for this is as follows: ");
    print("\tpython phylogeneticTree.py [-UPGMA / -Neighbor] [score_matrix] [outputFile]");
    print("Where:  -UPGMA is the tag for generating a UPGMA style tree and...");
    print("        -neighbor is the tag for generating a neighbor joining style tree.");
    print("       [score_matrix] is the file containing the matrix of the clustal scores for either tag");
    print("       [outputFile] is the optional file name where the tree will be printed to.");
    print("NOTE:  the output tree will be generated to the screen in all cases and will only be sent to a file if a name is provided");
    print("");
    print("");


################################################
###Matrix file Parser
################################################    
def parseMatrix(file):
    matrixFile = open(file,'r');
    line = matrixFile.readline();
    nodeLen = int(line.strip());

    line = matrixFile.readline();
    while line:
        if len(line) == 0:
            continue;
        names.append(line[0:10]);
        scores.append([float(n) for n in line[10:].split()]);
        line = matrixFile.readline();

########################################################################################################
########################################################################################################
###UPGMA Methods
########################################################################################################
########################################################################################################        
def UPGMA():
    print("Generating UPGMA tree...");
    
    for i in range(len(names)):
        active.append([i]);
    
    while len(active) > 2:
        c = closestClusters();
        updateActive(c);

def closestClusters():
    low = 999999.99;
    lowest = [];
    for i in range(len(active)-1):
        for j in range(i+1,len(active)):
            d = distance(i,j);
            if d < low:
                low = d;
                lowest = [i,j];
    
    return lowest;  ## where lowest is always [(smaller index), (larger index)]

def distance(i,j):
    distances = [];
    for k in range(len(active[i])):
        for l in range(len(active[j])):
            if active[i][k] > active[j][l]:
                distances.append(scores[active[i][k]][active[j][l]]);
            else:   
                distances.append(scores[active[j][l]][active[i][k]]);
    
    return sum(distances)/len(distances);
    
        
def updateActive(c):
    active[c[0]].extend(active[c[1]]);
    active.pop(c[1]);
    
    new = [];
    new.append(names.pop(c[1]));
    new.extend([names.pop(c[0])]);
    names.insert(c[1],new);

    
########################################################################################################
########################################################################################################
###Neighbor Joining Methods
########################################################################################################
########################################################################################################
def neighbor():
    print("Generating Neighbor joining tree...");
    
    tree = [];
    l = len(names);
    
    while len(names) > 2:
        legs = findLegWeights();
        u = lowestM(legs);
        u.sort();
        updateNames(u);
        u.reverse();
        updateMatrix(u);
    
##First Compute all Star Leg weights    
def findLegWeights():   
    weight = 0;
    legs = [];
    l = len(names);
    for n in range(l):
        for i in range(1,len(scores)):
            if i == n:
                for j in range(len(scores[i])):
                    weight += scores[i][j];
                continue;
            elif i < n:
                continue;
            else:
                weight += scores[i][n];
        legs.append(weight/(l-2));
        weight = 0;
    
    return legs;
    
##Next find the lowest M
def lowestM(legs):
    low = scores[1][0] - legs[1] - legs[0];
    ##lowest = [[names[1],names[0]]];
    lowest = [0,1];
    for i in range(1,len(scores)):
        for j in range(len(scores[i])):
            m = scores[i][j] - legs[i] - legs[j];
            if m < low:
                low = m;
                ##lowest = [names[i],names[j]];
                lowest = [i,j];
    
    return lowest;
    
## now update the names list
def updateNames(u):
    new = [];
    new.append(names.pop(u[1]));
    new.append(names.pop(u[0]));
    names.append(new);
    
#finally update the scores matrix   
def updateMatrix(u):
    ## for this method u = [ (larger index), (smaller index) ];
    ## dix will be for u[0] and djx for u[1]
    
    row = [];
    for i in range(len(scores)):
        if i != u[0] and i != u[1]:
            if i < u[0] and i < u[1]:
                dix = scores[u[0]][i];
                djx = scores[u[1]][i];
            elif i > u[0] and i > u[1]:
                dix = scores[i][u[0]];
                djx = scores[i][u[1]];
            else:  ## u[1] < i < u[0]
                dix = scores[u[0]][i];
                djx = scores[i][u[1]];
                
            d = dix + djx - scores[u[0]][u[1]];
            row.append(d);
        
    for l in range(len(u)):
        for i in range(1,len(scores)):
            if i == u[l]:
                for j in range(len(scores[i])):
                    if len(scores[i]) > 0:
                        scores[i].pop();
                    else:
                        continue;
            elif len(scores[i]) > u[l]:
                scores[i].pop(u[l]);
    scores.pop(u[0]);
    scores.pop(u[1]);
    scores.append(row);


########################################################################################################
########################################################################################################
###Tree Printing Method
########################################################################################################
########################################################################################################    
def printTree(output):
    print("Printing Tree..");
    if len(output) == 0:
        print("\tNo output file given.");
    else:
        print("\t...and printing to file: " + output);
        file = open(output, 'w');
    print("");
    print("");
    

    if len(output) > 0:
        file.close();
    
########################################################################################################
########################################################################################################
###Main Method
########################################################################################################
########################################################################################################
def main():
    
    usage();
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("But you entered an incorrect number of arguments, please run again with the correct usage described above");
        raise SystemExit
    elif not os.path.exists(sys.argv[2]):
        print("The matrix file that you eneterd does not exist or is named incorrectly, please run again with a proper file");
        raise SystemExit
    
    matrix = sys.argv[2];
    print("Parsing matrix file...");
    parseMatrix(matrix)
    
    outFile = '';
    
    if len(sys.argv) == 4:
        outFile = sys.argv[3];
        
    if sys.argv[1] == "-UPGMA":
        UPGMA();
    elif sys.argv[1] == "-neighbor":
        neighbor();
    else:
        print("You Entered an incorrect tag, please rerun with either -UPGMA or -neighbor");
        raise SystemExit
    
    print(names);
    
    if len(outFile) > 0:
        file = open(outFile, 'w');
        file.write(str(names));
        file.close();
    
if __name__ == "__main__":
    main()
