

package linkedlist;

/*
                            ▄▄ •  ▄▄▄· ▄▄▄▄▄ ▄▄▄· .▄▄ · 
                          ▐█ ▀ ▪▐█ ▀█ •██  ▐█ ▀█ ▐█ ▀. 
                         ▄█ ▀█▄▄█▀▀█  ▐█.▪▄█▀▀█ ▄▀▀▀█▄
                         ▐█▄▪▐█▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█


        _____              _     _         _      _       _            _ _      _     _   
       |  __ \            | |   | |       | |    (_)     | |          | | |    (_)   | |  
       | |  | | ___  _   _| |__ | |_   _  | |     _ _ __ | | _____  __| | |     _ ___| |_ 
       | |  | |/ _ \| | | | '_ \| | | | | | |    | | '_ \| |/ / _ \/ _` | |    | / __| __|
       | |__| | (_) | |_| | |_) | | |_| | | |____| | | | |   <  __/ (_| | |____| \__ \ |_ 
       |_____/ \___/ \__,_|_.__/|_|\__, | |______|_|_| |_|_|\_\___|\__,_|______|_|___/\__|
                                    __/ |                                                 
                                   |___/  


                            [DEQUEUE]

        *pop(E e) - Pops an element from the stack represented by this list.
       	*pollFirst() - Retrieves and removes the first element of this list, or returns null if this list is empty.
        *pollLast() - Retrieves and removes the last element of this list, or returns null if this list is empty.

                            [ENQUEUE]
        
        add(int index, E element) - Inserts the specified element at the specified position in this list.
        addFirst(E e) - Inserts the specified element at the beginning of this list. 
        addLast(E e) - Appends the specified element to the end of this list.


  
         

 */
public class LinkedList {

    public static SinglyLinkedList<Integer> singly = new SinglyLinkedList<>();
    public static DoublyLinkedList<Integer> doubly = new DoublyLinkedList<>(); 
    public static void main(String[] args) {
        System.out.println("Hell");
       
    }
}

class DoublyLinkedList<E> {
    
    private Node head;
    private Node tail;
    private int size;
    
/*========================================================================================        
/*========================================================================================        
/*========================================================================================
    
                        _____                                   
                       |  __ \                                  
                       | |  | | ___  __ _ _   _  ___ _   _  ___ 
                       | |  | |/ _ \/ _` | | | |/ _ \ | | |/ _ \
                       | |__| |  __/ (_| | |_| |  __/ |_| |  __/
                       |_____/ \___|\__, |\__,_|\___|\__,_|\___|
                                       | |                      
                                       |_|                          
                              [REMOVES THE VALUES]
   
        *pop(E e) - Pops an element from the stack represented by this list.
       	*pollFirst() - Retrieves and removes the first element of this list, or returns null if this list is empty.
       *pollLast() - Retrieves and removes the last element of this list, or returns null if this list is empty.

======================================================================================== */   
/*========================================================================================
 /*========================================================================================*/  
    
    
    
    
   // ==========================================================================   
   // [Pops an element from the stack represented by this list.]
   // ==========================================================================      
    public E pop(int index){
        if(index == 0){     
            return pollFirst();     // This will be inserted at the beggining of the list
        }else if(index == size-1){
            return pollLast();      // Inserted at the last index
        }else if( index > 0 && index < size){
            // Create Both Temporary to connect the temporay to a current node
            Node tmp = head;    
            Node tmp1 = head;
          
            for(int i = 1 ; i  < index ; i ++){
                tmp = tmp.next;
                tmp1 = tmp1.next;
            }
            
            E result = (E)tmp.next.value;   // Copy the value
            
            Node n = tmp;
            //         +---------------------------+
            //         |                           V
            // [. | v | .] - X > [. | v | .] -X > [. | v | .] 
            // Point the temporay to the next node  
            tmp = tmp.next.next;
            tmp.previous = n;
            tmp1.next = tmp1.next.next;
            size--;
            return result;
        }
        return null;
    }
    
    
    
    
    
   // ==========================================================================   
   //by 1 . If both did not match return false
   // After iteration return true
   // ========================================================================== 
    
    
    
    
   // ==========================================================================   
   // pollLast() - Retrieves and removes the last element of this list, or returns null if this list is empty.
   // ========================================================================== 
        public E pollLast(){
            if(head == null)return null;
            E result = (E)tail.value;   // Get the last value of the list 
            tail = tail.previous;       
            tail.next = null;
            size--;
            return result;
        
        }
    
    
    
    
    
    
    
    
   // ==========================================================================       
   // [  Retrieves and removes the last element of this list, or returns null if this list is empty. ]
   // ==========================================================================      
    public E pollFirst(){
           
        // If the list is empty . Just return null
        if(head == null)            
           return null;
        
        E val = (E) head.value;      // Get the pointer of the second node 
        if(size == 1){              // If the size only have one size . point the head 
            head = head.next;       // and the tail to a null value
            tail = tail.previous;
            size--;
            return val;
        }else{
            
            head = head.next;               // Point the head to its next value
            head.previous = null;            //   Remove the previous node
            size--;
        }       
           
        
        
        // Return the copied Node
        return val;
    }
   // ==========================================================================        
   // ==========================================================================   
    
    
    
  
    
    
    
    
    
/*========================================================================================        
/*========================================================================================        
/*========================================================================================
                    ______                                   
                   |  ____|                                  
                   | |__   _ __   __ _ _   _  ___ _   _  ___ 
                   |  __| | '_ \ / _` | | | |/ _ \ | | |/ _ \
                   | |____| | | | (_| | |_| |  __/ |_| |  __/
                   |______|_| |_|\__, |\__,_|\___|\__,_|\___|
                                    | |                      
                                    |_|                      
                               [INSERT THE VALUES]

       add(int index, E element) - Inserts the specified element at the specified position in this list.
       addFirst(E e) - Inserts the specified element at the beginning of this list. 
      addLast(E e) - Appends the specified element to the end of this list.

 =======================================================================================       
/*========================================================================================        
/*========================================================================================*/
    

   
   // ==========================================================================  
   // Inserts the specified element at the specified position in this list.
   // ========================================================================== 
   public void  add(int index ,E value){
        // If the index is 0 Just call the function addFirst[ add the node from the first element]
        if(index == 0){
            addFirst(value);
         // If the index is 0 Just call the function addLast[ add the node from the last element]
        }else if(index == size){
            addLast(value);
        }else if(index >0 && index < size){
            size++;
            Node val = new Node(value);
            Node node = head, temp = null;                   // Get all the list value and store it to node
            for(int i = 1 ; i < index ; i++){   // Loop through each until it reaches the condition
                node = node.next;
            }
            //      [.|v|.]
            //      /
            //[.|v|.]    -   [.|v|.]
            temp = node.next;           // Point the next pointer node to the list
            //       [.|v|.]
            //      //
            //[.|v|.]    -   [.|v|.]
            temp.previous =  node.next;       // Point the previous pointer to the node;
            
            //        [.|v|.]
            //      //      \\
            //[.|v|.]        [.|v|.]
            node.next = val;    // A node is added between a temporary node and the current node
            val.previous = node;
            val.next = temp;
            temp.previous =val;
         
          
            
            
        }else{
            
        }
    }
    
    
    
    
   // ==========================================================================  
   // ========================================================================== 
    

    
   // ==========================================================================  
   //  [ Inserts the specified element at the beginning of this list.  ] 
   // ========================================================================== 
    
    public void addFirst(E data){
        Node node = new Node(data); // Create Empty Node with Value 
        if(head == null){               // The list is empty
            head = node;                    // Initialized it with the node
            tail = node;  
            size++;
        }else{
           // [ .|.] < - [. | .] 
           head.previous = node;        //Point the head previous pointer to the node 
           // [ .|.] -> < - [. | .] 
           node.next = head;            // Point the node next pointer to the head
           head = node;                 // Initialize it
           head.previous = null;        // Point the previous to nulkl
           size++;
           
           
        }
    }
   // ==========================================================================  
   // ========================================================================== 
    
    
    
    
    
    
    
   
    
   // ==========================================================================  
   //[  Appends the specified element to the end of this list. ]
   // ========================================================================== 
    public void addLast(E data){
        
        Node node = new Node(null,data,null); // Create an empty node with value
        if(head == null){                       // If the list is empty
            head = node;                             //Initialized the node
            tail = node;
            size++;
            
        }else{              // Else
                                
                                        // [.| v |.] ->   [.| _ |.] ->   [.| n |.]  
            tail.next = node;           // Point the tail next pointer to the empty node   
                                        // [.| v |.] ->   [.| _ |.] ->   <-[.| n |.] 
            node.previous = tail;       // Point the last node to empty Node
            tail = node;                // Set the tail to the Node
            tail.next = null;           // Set the tail next pointer to null 
            size++;
            
        }
    }
    
   // ==========================================================================  
   // ========================================================================== 
    
    
    
   // ==========================================================================  
   // [Prints Backward]
   // ========================================================================== 
    
    public String back(){
        Node temp = tail;
        String r = "";
        while(temp!= null){
            r += temp.value+" ";
            temp = temp.previous ;
        }
      
        return "[ "+r+"]";
    }
    
   // ==========================================================================  
   // ========================================================================== 
    
    
    
    
   // ==========================================================================  
   // Print the list forward
   // ========================================================================== 
    public String toString(){
        Node temp = head;
        String r = "";
        while(temp != null){
            r += temp.value+ " ";
            temp = temp.next ;
        }
        return "[ "+r+"]";
    }
   // ==========================================================================  
   // ========================================================================== 
    
    
    
    
    
   // ==========================================================================  
   // Returns the size of list 
   // ========================================================================== 
    
    public int size(){
        return this.size;
    }
   // ==========================================================================  
   // ========================================================================== 
}

















/*
                            ▄▄ •  ▄▄▄· ▄▄▄▄▄ ▄▄▄· .▄▄ · 
                          ▐█ ▀ ▪▐█ ▀█ •██  ▐█ ▀█ ▐█ ▀. 
                         ▄█ ▀█▄▄█▀▀█  ▐█.▪▄█▀▀█ ▄▀▀▀█▄
                         ▐█▄▪▐█▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█
   
            _____ _             _        _      _       _            _ _      _     _   
           / ____(_)           | |      | |    (_)     | |          | | |    (_)   | |  
          | (___  _ _ __   __ _| | ___  | |     _ _ __ | | _____  __| | |     _ ___| |_ 
           \___ \| | '_ \ / _` | |/ _ \ | |    | | '_ \| |/ / _ \/ _` | |    | / __| __|
           ____) | | | | | (_| | |  __/ | |____| | | | |   <  __/ (_| | |____| \__ \ |_ 
          |_____/|_|_| |_|\__, |_|\___| |______|_|_| |_|_|\_\___|\__,_|______|_|___/\__|
                           __/ |                                                        
                          |___/   



                                [EXTRAS]
          list.Size()- get the size
          list.get(index)    - To access an element in the List
          list.set(index,value)    - change an item in the list with an index 
          list.clear() - Removes all the value from the list [reset]
          list.contains(value) - checks if the list has the value 
          list.isEmpty() - checks the list is empty or not 
          list.reverse() - it reverse the list 
          System.out.print(  name of the list ) ; prints the lists
        
                               [ ENQUEUE ]
          list.push(value);  This method can add one or more elements at the end of the list;
          list.unshift(value);   It add one or more elements to the beginning of the list;
          list.Insert(index,value) It add one or more elements to the list and insert it to a given index 
        
                                [DEQUEUE]
           list.pop() This method removes the last element from the given array and returns it.
           list.Shift() It delete the first element from the given array and returns it.
           list.remove(Index) It delete the index element from the given array and return

*/
   

class SinglyLinkedList<T> {
    
    
        Node head;  
        private int size;
        
        
/*========================================================================================        
/*========================================================================================        
/*========================================================================================
                    ______                                   
                   |  ____|                                  
                   | |__   _ __   __ _ _   _  ___ _   _  ___ 
                   |  __| | '_ \ / _` | | | |/ _ \ | | |/ _ \
                   | |____| | | | (_| | |_| |  __/ |_| |  __/
                   |______|_| |_|\__, |\__,_|\___|\__,_|\___|
                                    | |                      
                                    |_|                      
                               [INSERT THE VALUES]

        list.push(value);  This method can add one or more elements at the end of the list;
        list.unshift(value);   It add one or more elements to the beginning of the list;
        list.Insert(index,value) It add one or more elements to the list and insert it to a given index
 =======================================================================================       
/*========================================================================================        
/*========================================================================================*/
        
        
   // ==========================================================================  
   //[ This method can add one or more elements at the end of the list ]
   // ==========================================================================         
        
    public void push(T value){
        Node node = new Node();    // Converts value into node
        node.value = value;        // Create its own pointer
        if(head == null){
            head = node;
        }else{
            _push(node,head);     // Call the recursive functions
        }
        size++;
        
    }
    
    public Node _push(Node value,Node curNode){
        if(curNode.next != null){        // If not null Iterate 
            return _push(value,curNode.next);
        }
        curNode.next = value;
        return value;
    }
 // ==========================================================================        
 // ==========================================================================          
        
        
    
    
 // ==========================================================================    
 // [ It add one or more elements  to the beginning of an array.] 
 // ==========================================================================             
    public void unshift(T value){
        Node node = new Node();         // Call the list 
        node.value = value;             //Convert the data into node
        node.next = head;               //  Point the pointer to the head
        head = node;                    //  set the head to data 
        size ++;
    }
 // ==========================================================================        
 // ==========================================================================                 
        
        
        
    
   // ==========================================================================  
   // [ It add one or more elements to the list and insert it to a given index ]
   // ========================================================================== 
   
   public void Insert(int index,T value){
        if(index == 0){                        // If index is zero just call the unshift 
            unshift(value);                     // (RJust point the value to the head)
        }
        else if(index <= size && index >0){ 
            size++; 
            Node node = new Node();             // Create an empty Node 
            node.next = null ;                  // Then point it to null
            node.value = value;                 // with a given value [ value , pointer ]
            Node n = head;                      // Then start the index 
            for(int i = 0 ; i < index-1 ; i ++){    // Loop through values until riches the given index
                n = n.next;
            }
            Node nextSlide = n.next;            // Copy the next value before the pointer
            n.next = node;                      // Insert the node
            n.next.next= nextSlide;             // Then point it to copied nodes 
            while(n.next != null){             
                n = n.next;
            }

        }else{                                                  
            System.out.println("  : OutOfBounce Exception ");  // Index Out of Bounce
        }
    }
   
   // ==========================================================================       
   // ========================================================================== 
   
        
   
   
        
        
/*========================================================================================        
/*========================================================================================        
/*========================================================================================
    
                        _____                                   
                       |  __ \                                  
                       | |  | | ___  __ _ _   _  ___ _   _  ___ 
                       | |  | |/ _ \/ _` | | | |/ _ \ | | |/ _ \
                       | |__| |  __/ (_| | |_| |  __/ |_| |  __/
                       |_____/ \___|\__, |\__,_|\___|\__,_|\___|
                                       | |                      
                                       |_|                          
                              [REMOVES THE VALUES]
   
           list.pop() This method removes the last element from the given array and returns it.
           list.Shift() It delete the first element from the given array and returns it.
           list.remove(Index) It delete the index element from the given array and return
======================================================================================== */   
/*========================================================================================
 /*========================================================================================*/   
        
        
        
   // ==========================================================================  
   //[This method removes the last element from the given array and returns it.]
   // ========================================================================== 
   public T pop(){
        Node node = head;
        if(head == null)                    // Checks if the list if empty
            return null;
        if(size>1){                         // If it was greater than 1
            while (node.next.next != null){     // Loop through each until it reachs the second to the last value
                node = node.next;               // Pointer the value to the next value
            }
            size --;   
            T val = (T) node.next.value;    // if it hits the second to the last . Copy the last value
            node.next = node.next.next;     // Removes the last value
            return val;                     // Return the current value
        }else if(size == 1){
            Node n = new Node();            // If it only has 1 value
            T val = (T) n.value;            // Copy the first value
            head = n.next;                  // Reset the list
            size --;    
            return val;                     // Return the current value
        }
        return null;
    }
        
   
   // ==========================================================================        
   // ==========================================================================       
        
        
   
   
        
        
        
   // ========================================================================== 
   //    [ It delete the first element from the given array and returns it. ]
   // ==========================================================================
    public T shift(){
        T val = (T) head.value; // copy the first value
        head = head.next;       // removes the first value
        size--;                 
        return val;             // Returns the copied value
    }
   // ==========================================================================       
   // ==========================================================================   
        
        

        
        
   // =============================================================================
   // remove(Index) It delete the index element from the given array and returns it.
   // =============================================================================
   
    public T remove(int index){
        if(index == 0){
            return shift();          // if the index is 0 then just call the shift( Removes the first value)
        } else if(index < size){
            Node node = head;                   // Create node 
            for(int i = 1 ; i < index ; i ++){  // loop through each
                node = node.next;               
            } 
            T val = (T) node.next.value;        // Copy the value
            node.next = node.next.next;         // Remove is
            size--;
            return val;                         // Return the coppied value
        }else{
            return null;                        // if it was empty return null
        }
    }      
    // ========================================================================    
    // ========================================================================         
        
        
        
        
        
        
        

        
    /*========================================================================================
                                         [EXTRAS]
    
             list.Size()- get the size
             list.get(index)    - To access an element in the List
             list.set(index,value)    - change an item in the list with an index 
             list.clear() - Removes all the value from the list [reset]
             list.contains(value) - checks if the list has the value 
             list.isEmpty() - checks the list is empty or not 
             list.reverse() - it reverse the list 
             System.out.print(  name of the list ) ; prints the lists

    ========================================================================================*/
        
        
        
        

   // ==========================================================================
   //   list.set(index,value)    - change an item in the list with the given index 
   // ==========================================================================
    public void set(int index , T value){
        Node val = new Node();
        val.value = value;
        val.next  =null;
        if(index  == 0 & size >0){      // the user input the 0 just change the head 
            Node node = new Node();     // Create empty node
            node.value = value; //      // Convert the data into node
            node.next = head;           // Point the pointer to the head   
            head = node;                // set the head to data 
            Node n= head;                
            n.next = n.next.next;       // Removes the second node 

        }else if(size >0 && index <size ){
           Node n = head;
           for(int i = 1 ; i < index ; i ++){
               n = n.next;
           } 
           // Copy the next next node then connect it to the replaces value
           
           Node shft = n.next.next;
           n.next = val;
           n.next.next = shft;
       }
    }     
   // ==========================================================================    
   // ==========================================================================     
        
        
   // ==========================================================================
   //           Return the value of the index that user inputted
   // ==========================================================================
   public T get(int index){
        if(head == null)        // If the list is empty return null
            return null;
        if(size >=0 && index <size && size >=0){
            Node n = head;
            for(int i = 0 ; i < index ; i++){
                n = n.next;
            }
            return (T) n.value;
        }else{
            return null;
        
        }
    }
   // ==========================================================================
   // ==========================================================================
   
   
   
   
   // ==========================================================================    
   //                         [Clears the whole list]
   // ==========================================================================
    public void clear(){
        head = null;
        size = 0 ;
    }
     // ========================================================================
     
     
     
        
    //==============[Checks if your list has the value you've looking for]======    
    public boolean contains(T value){
        if(head == null){                       // If it was empty 
            return false;
        }
        Node n = head;
        while(n != null){                      // Loop through each
            if((value+"").equals(n.value+""))  // It converts to string then compare
                return true;
            n = n.next;
        }
        return false;
    }
    //========================================================================== 
    

    
        
    //==========================================================================
    public boolean isEmpty(){
        return head == null; // if head is null then it is empty else it is not
    }
    //==========================================================================
    
    
    
    
        
        
    // =========================[Size of the List ]=============================
     public int size(){
        return this.size;
    }
    // =========================================================================
        
        
     
     
    // =====================[Prints all the value ]=============================
    public String toString(){
        
        if(size <=0)
            return "{ }";
        Node node = head;
        String print = "";
        while(node != null){
            print += node.value+" ";
            node = node.next;
        }
      
        return "[ "+print+"]";
    }
    // =========================================================================
    
    
    // =========================================================================
    //                      [ REVERSED ALL THE LIST ]
    // =========================================================================
    public void reverse(){
        if(head != null){                       // IF head is not null
            Node prev = new Node(head.value);   // Get the first value
            Node curNode = head.next;           // Get all the value of the list except the first value
            while(curNode!= null){              // Loop Through each    
                Node nxt = curNode.next;            // Get the next value and store it
                curNode.next = prev;                // Point the next value to the previous value
                prev = curNode;                     // Get the previous value and store it to prev
                curNode = nxt;                      // Get the next pointer before the pointer rotation happened
            }
            head =prev ;                        // Set the list to stored reversed value 
        }
       
    }
    // =========================================================================
   
}









/*
            ▄▄ •  ▄▄▄· ▄▄▄▄▄ ▄▄▄· .▄▄ · 
          ▐█ ▀ ▪▐█ ▀█ •██  ▐█ ▀█ ▐█ ▀. 
         ▄█ ▀█▄▄█▀▀█  ▐█.▪▄█▀▀█ ▄▀▀▀█▄
         ▐█▄▪▐█▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█
*/


class Node<T> {
    
    public T value;
    public Node next ;
    public Node previous;
    
    public Node(T value){
        this.previous = null;
        this.value = value;
        this.next = null;
    }
    
    public Node(Node previous,T value,Node next){
        this.previous = previous;
        this.value = value;
        this.next = next;
    }

    public Node(){
        this.previous = null;
        this.value = null;
        this.next = null;
    
    }
    public T Value(){
        return this.value;
    }
    
}