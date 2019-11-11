import math

def main():
    theta = 0
    
    Vertices = []
    for theta in range(0,360,(360//32)):
        print(theta)
        Vertices.append((math.cos(math.radians(theta)),1,math.sin(math.radians(theta))))
        Vertices.append((math.cos(math.radians(theta)),-1,math.sin(math.radians(theta))))
        
    #get vertices
    for i in range(0,len(Vertices)): 
        print(Vertices[i],"\n")
    
    #draw faces
    UpperFaces = [];
    for i in range(67,3,-2):
        UpperFaces.append((i-2,1,i))
    
    for i in range(len(UpperFaces)):
        print(UpperFaces[i])
    
    LowerFaces = []
    for i in range(68,4,-2):
        LowerFaces.append((i,2,i-2))    
    
    UpperMiddleFaces = []
    for i in range(68,4,-2):
        UpperMiddleFaces.append((i-2,i-1,i))
    
    LowerMiddleFaces = []
    for i in range(67,4,-2):
        LowerMiddleFaces.append((i,i-1,i-2))
    
    f = open("CylinderSmoothv2.obj","w+")
    #input all the vertices
    
    #these are the center vertices
    f.write("v %d %d %d\n" %(0,1,0)) #v1
    
    f.write("v %d %d %d\n" %(0,-1,0)) #v2
    for i in range(len(Vertices)):
        f.write("v %f %f %f\n" % (Vertices[i][0],Vertices[i][1],Vertices[i][2]))
        
    #write the normals
    f.write("vn %d %d %d\n" %(0,1,0))
    f.write("vn %d %d %d\n" %(0,-1,0))
    for i in range(len(Vertices)):
        f.write("vn %f %f %f\n" % (Vertices[i][0],Vertices[i][1],Vertices[i][2]))
        
    
    #input the faces
    #upperface
    for i in range(len(UpperFaces)):
        f.write("f %d//%d %d//%d %d//%d\n" % (UpperFaces[i][0],UpperFaces[i][0],UpperFaces[i][1],UpperFaces[i][1],UpperFaces[i][2],UpperFaces[i][2]))
    #last upper face
    f.write("f %d//%d %d//%d %d//%d\n" % (67,67,1,1,3,3))
    
    #lowerface
    for i in range(len(LowerFaces)):
        f.write("f %d//%d %d//%d %d//%d\n" % (LowerFaces[i][0],LowerFaces[i][0],LowerFaces[i][1],LowerFaces[i][1],LowerFaces[i][2],LowerFaces[i][2]))
    #last lower face
    f.write("f %d//%d %d//%d %d//%d\n" % (4,4,2,2,68,68))
    
    #middle faces
    for i in range(len(UpperMiddleFaces)):
        f.write("f %d//%d %d//%d %d//%d\n" % (UpperMiddleFaces[i][0],UpperMiddleFaces[i][0],UpperMiddleFaces[i][1],UpperMiddleFaces[i][1],UpperMiddleFaces[i][2],UpperMiddleFaces[i][2]))
        
    for i in range(len(LowerMiddleFaces)):
        f.write("f %d//%d %d//%d %d//%d\n" % (LowerMiddleFaces[i][0],LowerMiddleFaces[i][0],LowerMiddleFaces[i][1],LowerMiddleFaces[i][1],LowerMiddleFaces[i][2],LowerMiddleFaces[i][2]))    
    #last middle face
    f.write("f %d//%d %d//%d %d//%d\n" % (68,68,3,3,4,4))
    f.write("f %d//%d %d//%d %d//%dd\n" % (3,3,68,68,67,67))
    f.close()