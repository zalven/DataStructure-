/******************************************************************************
    Zalven Lemuel S. Dayao 1BSCS2 . 1st year ComSci

             ▄▄ •  ▄▄▄· ▄▄▄▄▄ ▄▄▄· .▄▄ · 
            ▐█ ▀ ▪▐█ ▀█ •██  ▐█ ▀█ ▐█ ▀. 
            ▄█ ▀█▄▄█▀▀█  ▐█.▪▄█▀▀█ ▄▀▀▀█▄
            ▐█▄▪▐█▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█

*******************************************************************************/
import java.util.*;
public class  trees extends tools {
    public static void main(String[] args) {
        process();
    }
    private static void process(){
        int input = 0;
        do{
            printChoices();
            input = intInput("Enter choices : ");
            choices(input);
        }while(input <4 );
    }
    private static void choices(int input){
        if(input == 1){
            BinarySearchTrees();
            resetTrees();
        }else if(input == 2){
            AVLTrees();
            resetTrees();
        }else if(input == 3){
            ExpTree();
            resetTrees();
        }else{
            resetTrees();
        }
    }


}



//============================================================================================================


class tools{

    public static Scanner scan = new Scanner(System.in);
    public  static  TreeTraversal<String> printStr = new TreeTraversal<String>();
    public static  TreeTraversal<Integer> printNum = new TreeTraversal<Integer>();
    public static  ExpressionTree exp = new ExpressionTree();

    // infixToTree( String )    Converts expression to tree
    // eval()                   Evaluate the tree

    public static void ExpTree(){
        try{
            Scanner s =  new Scanner(System.in);
            System.out.print(" [0-9]Enter Operations: ");
            String input = s.nextLine();
            exp.infixToTree(input);
        }catch(Exception e){}
        try{System.out.println("Evaluation : "+exp.eval());
        }catch(Exception e){}
        printStr.display( exp.get() );
    }
// size()           Size of the Tree 
// maxDepth()       max Depth of the tree
// maxDepth()       min Depth of the tree 
// insert(key)      Insertion
// delete(key)      deletion 
// search(key)      Search     
// get()            get the tree node 



    private static BinarySearchTree bst = new BinarySearchTree();
    public static void BinarySearchTrees(){
        int input = 0 ;
        do{
            menuBSTandAVL();
            input = intInput("[BST]Enter choice : ");
            BSTchoices(input);
        }while(input != 7);
           
    }
    private static void  BSTchoices(int choice){
        if(choice == 1)  bst.insert( intInput("Enter value : ") );
        if(choice == 2)  bst.delete( intInput("Enter value : ") );
        if(choice == 3)  System.out.println( bst.search(  intInput("Enter value : ")     ));
        if(choice == 4)  printNum.display(bst.get() );
        if(choice == 5)  System.out.println( "size "+bst.size() );
        if(choice == 6)  System.out.println("max : "+bst.maxDepth() +"   min : "+bst.minDepth() ) ; 
    }   

    public static void resetTrees(){
        bst = new BinarySearchTree();
        avl = new AvlTree();
        exp  = new ExpressionTree();
    }

    private static AvlTree avl = new AvlTree();
    public static void AVLTrees(){
        int input = 0 ;
        do{
            menuBSTandAVL();
            input = intInput("[BST]Enter choice : ");
            Avlchoices(input);
        }while(input != 7);
    }
    private static void  Avlchoices(int choice){
        if(choice == 1)  avl.insert( intInput("Enter value : ") );
        if(choice == 2)  avl.delete( intInput("Enter value : ") );
        if(choice == 3)  System.out.println(avl.search(  intInput("Enter value : ")     ));
        if(choice == 4)  printNum.display(avl.get() );
        if(choice == 5)  System.out.println( "size "+avl.size() );
        if(choice == 6)  System.out.println("max : "+avl.maxDepth() +"   min : "+avl.minDepth() ) ; 
    }   


    public static Integer intInput(String message){
        System.out.println("======================================");
        System.out.print(message);
        return scan.nextInt();
    }
    public static String strInput(String message){
        Scanner s =  new Scanner(System.in);
        System.out.println("======================================");
        System.out.print(message);
        return s.nextLine();
    }
    public static void printChoices(){
        System.out.println("-------------------------------------");
        System.out.println("1.) Binary Search Tree ");
        System.out.println("2.) AVL Tree ");
        System.out.println("3.) Expression Tree ");
        System.out.println("4.) Exit ");
        System.out.println("-------------------------------------");
    }
    public static void menuBSTandAVL(){
        System.out.println("-------------------------------------");
        System.out.println("1.) Input number ");
        System.out.println("2.) Delete number");
        System.out.println("3.) check value exist");
        System.out.println("4.) display tree ");
        System.out.println("5.) get size ");
        System.out.println("6.) get height");
        System.out.println("7.) Exit");
        System.out.println("-------------------------------------");
    }


    

}



//============================================================================================================
// infixToTree( String )    Converts expression to tree
// eval()                   Evaluate the tree


class ExpressionTree{
    private TreeNode<String> root;
    private double result =  0;
    
    //======================================================
    public TreeNode<String> get(){
        return root;
    }
    //======================================================
    public TreeNode<String> infixToTree( String value){
        root = _infixToTree(root,value); 
        return root;
    }
    //======================================================

    public double eval(){
        return _eval(root);
    }
    //======================================================
    private double _eval( TreeNode<String> root ){
        if(root == null)
            return 0;
        if(root.left == null  && root.right == null )
            return Integer.parseInt(root.value);
        double left = _eval(root.left);
        double right = _eval(root.right);
        if(root.value.equals("+"))
            return left+right;
        if(root.value.equals("-"))
            return left-right;
        if(root.value.equals("/"))
            return left / right;
        return left/right;
    }

//======================================================
    private TreeNode<String> _infixToTree(TreeNode<String> root , String value){
        if(!value.equals("")){
            value = outerParenthesisRemover(value);
            int index = findLowestValue(value);
            root = new TreeNode<String>( value.charAt(index)+"" );
            root.left = _infixToTree(root.left,  value.substring(0,index) );
            root.right = _infixToTree(root.right, value.substring(index+1) );
        }
        return  root ;
    }
    //======================================================


    private String outerParenthesisRemover(String value){
        if( removeEndParenthesis(value) && value.length() >= 2) 
            value =  value.substring(1,value.length()-1) ;
        return value;
    }
    //======================================================
    private int findLowestValue(String value){
        int result = 0,index = 0 , minValue = 5 , len = value.length(), parenthesis = 0;
        for(index = 0 ; index < len; index++){
            char chr = value.charAt(index);
            if(chr == '(')parenthesis++;
            if(chr == ')') parenthesis--;
            if( parenthesis == 0){
                if( precedence( chr ) <= minValue && isOperator(chr) ){
                    minValue = precedence( chr ) ;
                    result = index;
                }
            }
        }
        
        return result;
    }
    //======================================================
    private boolean isOperator(char val){
        return val == '+' || val == '-' || val == '*' || val == '/' || val == '^';
    }
//======================================================
    private boolean removeEndParenthesis(String value){
        int index = 0, parenthesis = 0 , len = value.length() , zeroes =0;

        while(index < len){
            char val = value.charAt(index++);
            if(val == '(')parenthesis ++;
            if(val == ')') parenthesis--;
            if(parenthesis == 0 &&  val == ')') zeroes++;
            if(zeroes >=2)
                return false;
        }
        return zeroes == 1;
    }
//======================================================
    private int precedence(char value){
        if(value == '+'||value == '-')
            return 1;
        if(value == '/' || value == '*')
            return 2;
        if(value == '^')
            return 3;
        return 4;
    }
    
}
//============================================================================================================















//============================================================================================================
// size()           Size of the Tree 
// maxDepth()       max Depth of the tree
// minDepth()       min Depth of the tree 
// insert(key)      Insertion
// delete(key)      deletion 
// search(key)      Search     
// get()            get the tree node 
class AvlTree{

    private TreeNode<Integer> root;
    private  int size = 0;

     
    //======================================================
    public boolean search( Integer key){
        if(root == null) return false;
        return _search(root,key);
    }
    private boolean _search( TreeNode<Integer> root ,  Integer key  ){
        if(root != null)
            if(root.value == key)  return true;
            else if(key < root.value ) return _search(root.left ,key  );
            else if(key > root.value)  return _search(root.right ,key  );
        return false;
    }
    //======================================================
    // Deletion 
    //======================================================//======================================================
    //======================================================//======================================================
  
   
    public TreeNode<Integer> delete( Integer key){
        root = _delete(root,key);
        return root;
    }
    private TreeNode<Integer> _delete( TreeNode<Integer> root , Integer key){
        if( root == null )return root;
        else if( key < root.value ) root.left = _delete(root.left, key) ;
        else if (key > root.value) root.right = _delete(root.right , key);
        else{
            if(root.right== null) return root.left;
            if(root.left == null) return root.right;
            
            root.value = getValue(root.left );
            root.left  = _delete(root.left  ,root.value);
            producHeight(root);

            Integer below = getBelowValue(root);
            if(below != null) root = balanceTheTree(root,below); 
           
        }
        return root;
    }
    //======================================================
    private Integer getBelowValue( TreeNode<Integer> root ){
        if(root == null)   return null;
        if(root.left != null && root.left.left   != null)   return root.left.left.value;
        if(root.left != null && root.left.right  != null)   return root.left.right.value;
        if(root.right!= null && root.right.right != null)   return root.right.right.value;
        if(root.right!= null && root.right.left  != null)   return root.right.left.value;
        return null;
    }
    //======================================================
    private Integer  getValue(TreeNode<Integer> root){
        while(root.right != null) 
            root = root.right ;
        return root.value;
    }
    //======================================================



    //======================================================//======================================================
    //======================================================//======================================================
    //======================================================//======================================================
    // Insertion
    public  TreeNode<Integer> insert(Integer key){
        root = _insert(root,key);
        return root;
    }
    //======================================================
    private TreeNode<Integer> _insert( TreeNode<Integer> root , Integer key){

        if(root == null)             return new TreeNode<Integer>(key);
        if(key < root.value )        root.left = _insert( root.left , key );
        else if(key > root.value )   root.right = _insert(root.right, key);  


        producHeight(root);
        return balanceTheTree(root,key);
    }
    //======================================================
    private void producHeight(  TreeNode<Integer>  root   ){
        root.height = Math.max(  getHeight(root.left) , getHeight(root.right)  )+1;
    }
    //======================================================
    private  TreeNode<Integer> balanceTheTree( TreeNode<Integer> root  ,Integer  key  ){
        int balance = balanceValue(root) ;
        if( balance >  1 && key < root.left.value  )  return  leftRotate(root);
        if( balance < -1 && key > root.right.value )  return  rightRotate(root);
        if( balance >  1 && key > root.left.value  )  return  rightLeftRotate(root);
        if( balance < -1 && key < root.right.value )  return  leftRightRotate(root);
        return root;
    }
    //======================================================
    private TreeNode<Integer>  leftRightRotate(TreeNode<Integer> root ){
        root.right  =  leftRotate(root.right);
        return rightRotate(root);
    }
    //======================================================
    private TreeNode<Integer> rightLeftRotate(TreeNode<Integer> root ){
        root.left =  rightRotate(root.left);
        return leftRotate(root);
    }
    //======================================================
    private TreeNode<Integer> rightRotate( TreeNode<Integer> root  ){
        System.out.println("rigt - "+root.value );
        TreeNode<Integer> rightNode = root.right;
        TreeNode<Integer> leftNode = rightNode.left;
        rightNode.left = root;
        root.right = leftNode;
        rightNode.height = Math.max( getHeight(rightNode .right)    ,  getHeight(rightNode .left))+1;
        root.height = Math.max( getHeight(root.right)    ,  getHeight( root.left))+1;
        return rightNode;
    }
    //======================================================
    private TreeNode<Integer> leftRotate( TreeNode<Integer> root  ){
        System.out.println(root.value);
        TreeNode<Integer> leftNode = root.left;
        TreeNode<Integer> rightNode = leftNode.right;
        leftNode.right   = root;
        root.left = rightNode;
        leftNode .height = Math.max( getHeight(leftNode .right)    ,  getHeight(leftNode .left))+1;
        root.height = Math.max( getHeight(root.right)    ,  getHeight( root.left))+1;
        return  leftNode;
    }
    //======================================================
    private int balanceValue(  TreeNode<Integer> root ){
        return root == null?0: getHeight(root.left) - getHeight(root.right);
    }
    //======================================================
    private int getHeight(  TreeNode<Integer> root  ){
        return root == null? 0 : root.height;
    }
    //======================================================//======================================================

    //======================================================
    public TreeNode<Integer> get(){
        return root;
    }
   //======================================================

   public int minDepth(){
    return  _minDepth(root);
}
private int _minDepth( TreeNode<Integer> root) {
    if(root == null)
        return 0;
    if(root.left == null && root.right == null)
        return 1;
     int left = _minDepth(root.left);
     int right = _minDepth(root.right);
    if(left == 0 || right== 0)
        return Math.max(left,right) + 1;
    return Math.min(left,right) + 1;
}
//======================================================
public int maxDepth() {
    return _depth(root);
}
private int _depth( TreeNode<Integer> root){
    if(root == null)   return 0;
    return 1 + Math.max(_depth(root.left), _depth(root.right));
}
//======================================================
//======================================================
public int size(){
    return this.size;
}
//======================================================


}
//============================================================================================================
















//============================================================================================================
// size()           Size of the Tree 
// maxDepth()       max Depth of the tree
// maxDepth()       min Depth of the tree 
// insert(key)      Insertion
// delete(key)      deletion 
// search(key)      Search     
// get()            get the tree node 
class BinarySearchTree{
  
    private int size;
    private TreeNode<Integer> root;
    //======================================================
    public TreeNode<Integer> get(){
        return root;
    }
 
    //======================================================
    public boolean search( Integer key){
        if(root == null) return false;
        return _search(root,key);
    }
    private boolean _search( TreeNode<Integer> root ,  Integer key  ){
        if(root != null)
            if(root.value == key)  return true;
            else if(key < root.value ) return _search(root.left ,key  );
            else if(key > root.value)  return _search(root.right ,key  );

        return false;
    }
    //======================================================


    //======================================================
    //          [Delete node]
    public TreeNode<Integer> delete( Integer key){
        if(root != null)
            root = _deleteNode(root,key);
        return root;
    }

    private TreeNode<Integer> _deleteNode( TreeNode<Integer> root,  Integer key) {
        if(root == null) {
            size--;
            return root;
        }
        if(key < root.value) 
            root.left = _deleteNode(root.left, key);
        else if(key > root.value) 
            root.right = _deleteNode(root.right, key);
        else{
            if(root.left == null) return root.right;
            else if(root.right == null) return root.left;
            root.value = getValue(root.right);
            root.right = _deleteNode(root.right, root.value);
        }
        return root;
    }
    private Integer getValue(TreeNode<Integer> root){
        while(root.left != null) 
            root = root.left;
        return root.value;
    }
    
    //======================================================
    //                  [INSERTION]
    public TreeNode<Integer> insert( Integer key){
        root = _insert(root,key);
        return root;
    }
    private TreeNode<Integer> _insert(TreeNode<Integer> root, Integer key){
        if(root == null){ size ++; return new TreeNode<Integer>(key);}
        if(key < root.value) root.left = _insert(root.left,key);
        if(key > root.value)  root.right = _insert(root.right,key);
        return root;
    }
    //======================================================

    public int minDepth(){
        return  _minDepth(root);
    }
    private int _minDepth( TreeNode<Integer> root) {
        if(root == null)
            return 0;
        if(root.left == null && root.right == null)
            return 1;
         int left = _minDepth(root.left);
         int right = _minDepth(root.right);
        if(left == 0 || right== 0)
            return Math.max(left,right) + 1;
        return Math.min(left,right) + 1;
    }
    
    //======================================================
    public int maxDepth() {
        return _depth(root);
    }
    private int _depth( TreeNode<Integer> root){
        if(root == null) 
            return 0;
        return 1 + Math.max(_depth(root.left), _depth(root.right));
    }
    //======================================================


    //======================================================
    public int size(){
        return this.size;
    }
    //======================================================


}
//============================================================================================================
































//============================================================================================================
//  [ TRAVERSE ]
// postOrder(node)       Post-Order Traversal 
// preOrder(node)        Pre-Order Traversal
// inOrder(node)         In-Order Traversal 
// displayTree(node)     Tree display
// display()             display all 
class TreeTraversal<E>{
    private String print = "";

    //======================================================
    public String postOrder( TreeNode<E>  root){
        print = "";
        if(root == null)
            return "Post-Order : [ "+print+" ]";
        _postOrder(root);
        return "Post-Order : [ "+print+" ]";
    }
    //======================================================
    public String preOrder( TreeNode<E>  root){
        print = "";
        if(root == null)
            return "Pre-Order : [ "+print+" ]";  
        _preOrder(root);      
        return "Pre-Order : [ "+print+" ]";
    }
    //======================================================
    public String inOrder( TreeNode<E>  root){
        print = "";
        if(root == null)
            return "in-Order : [ "+print+" ]";   
        _inOrder(root);  
        return "in-Order : [ "+print+" ]";
    }
 
    //======================================================
    public void displayTree(TreeNode<E> root){
        
        System.out.println("======================================");
        System.out.println("            [TREE]          ");
         List<List<String>>  tree =  printTree(root);
        for( List<String> leaf : tree){
            for( String node: leaf)
                System.out.print( node.equals("") ? " " : node );
            System.out.println();
        }
        
        System.out.println("======================================");
    
    }
    //======================================================
    public void display( TreeNode<E> root){
        System.out.println();
        System.out.println();
        System.out.println("======================================");
        displayTree(root);
        System.out.println( postOrder (root));
        System.out.println( preOrder(root) );
        System.out.println( inOrder(root));
        System.out.println("======================================");
        System.out.println();
        System.out.println();
        
    }
    //======================================================
    private void _postOrder(TreeNode<E>  root){
        if(root != null){
            _postOrder(root.left);
            _postOrder(root.right);
            print += root.value+", ";
        }
    }

    //======================================================
    private void _preOrder( TreeNode<E>  root){
        if(root != null){
            print += root.value+", ";
            _preOrder(root.left);
            _preOrder(root.right);
        }
    }
    //======================================================
    private void _inOrder( TreeNode<E>  root){
        if(root != null){
            _inOrder(root.left);
            print += root.value+", ";
            _inOrder(root.right);
        }
    }
    //======================================================
    private List<List<String>> printTree( TreeNode<E> root) {
         List<List<String>> result = new ArrayList<List<String>>();
        if(root == null) 
            return result;
        int height = depth(root); 
        int size = (int)Math.pow(2, height) - 1;
        Queue<TreeNode> parents = new ArrayDeque<>();

        parents.add(root);


        Queue<Integer> indexes = new ArrayDeque<>();
        indexes.add(size/2);  
        while(!parents.isEmpty()){

            Queue<TreeNode> tempParents = new ArrayDeque<>();
            Queue<Integer> tempIndexes = new ArrayDeque<>();
            List<String> list = createList(size);


            while(!parents.isEmpty()){
                int curIndex = indexes.poll(); 
                TreeNode node = parents.poll(); 
                list.set(curIndex, node.value+"");
                int nextIndex = (int) Math.pow(2, height - 2);;
                if(node.left != null){
                    tempParents.add(node.left); 
                    tempIndexes.add(curIndex - nextIndex);
                }
                if(node.right != null){
                    tempParents.add(node.right); 
                    tempIndexes.add(curIndex + nextIndex);
                }
            }
            result.add(list);
            height--; 
            parents = tempParents; 
            indexes = tempIndexes; 
        }
        return result;
    }
    //======================================================
    private List<String> createList(int size){
        List<String> list = new ArrayList<>();
        for(int i = 0; i < size; ++i){
            list.add("");
        }
        return list;
    }
    
    //======================================================
    private int depth( TreeNode root){
        if(root == null) return 0;
        return 1 + Math.max(depth(root.left), depth(root.right));
    }
    //======================================================    

}





//============================================================================================================




//============================================================================================================
//                      [TREE NODE]
class TreeNode<E> {


    
    E value;
    TreeNode<E> left;
    TreeNode<E> right;
    int height;

    public TreeNode( E value) {
        this.value = value;
        this.left = null;
        this.right = null;
        this.height = 1;
    }
    public TreeNode(){
        this.value = null;
        this.left= null;
        this.right = null;
        this.height =  0;
    }
  
}
