

class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.right=None
        self.left=None
    

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)
    
def level_order(root):
    q = []
    q.append(root)
    while len(q) != 0:
        p=q[0]
        q.pop(0)
        print(p.val)
        if p.left != None:
            q.append(p.left)
        if p.right != None:
            q.append(p.right)
            
def height(root):
    if root==None:
        return 0
    left=height(root.left)
    right=height(root.right)
    return max(left,right)+1   
        
def main():
    val=int(input())
    root=Node(val)
    q=[]
    q.append(root)
    while len(q)!=0:
        p=q[0]
        q.pop(0)
        a=int(input())
        b=int(input())
        left=None
        right=None
        if a!=-1:
            left=Node(a)
        if b!=-1:
            right=Node(b)
        p.left=left
        p.right=right
        if p.left!=None:
            q.append(p.left)
        if p.right!=None:
            q.append(p.right)
            
    inorder(root)
    print()
    level_order(root)
    print()
    print(height(root))

main()

"""
10
20
30
40
-1
-1
50
-1
-1
-1
-1

10
20
30
40
-1
-1
50
-1
-1
-1
-1

10
20
30
40
-1
-1
50
-1
-1
-1
-1
"""