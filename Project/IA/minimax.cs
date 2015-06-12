using System;
using System.Collections;



class Node
{
    double probability = 1.0;
    ArrayList children;
    int IALife = 100;
    int PLife = 100;
    int hit = 0;
    string type = "max";

    public Node(double probability, ArrayList children, int IALife, int PLife, int hit, string type)
    {
        this.probability = probability;
        this.children = children;
        this.IALife = IALife;
        this.PLife = PLife;
        this.hit = hit;
        this.type = type;
    }

    public double getProbability()
    {
        return this.probability;
    }
    public void setProbability(double probability)
    {
        this.probability = probability;
    }

    public ArrayList getChildren()
    {
        return this.children;
    }
    public void setChildren(ArrayList children)
    {
        this.children = children;
    }

    public int getIALife()
    {
        return this.IALife;
    }
    public void setIALife(int IALife)
    {
        this.IALife = IALife;
    }

    public int getPLife()
    {
        return this.PLife;
    }
    public void setPLife(int PLife)
    {
        this.PLife = PLife;
    }

    public int getHit()
    {
        return this.hit;
    }
    public void setHit(int hit)
    {
        this.hit = hit;
    }

    public string getType()
    {
        return this.type;
    }
    public void setType(string type)
    {
        this.type = type;
    }
}

class minimax
{
    double[] prob1 = new double[2] { 0.8, 0.5 }; //probabilidad de acertar
    double[] prob2 = new double[2] { 0.1, 0.4 }; //probabilidad de no pegar
    double[] prob3 = new double[2] { 0.1, 0.1 }; //probabilidad de pegar doble
    int[] hit1 = new int[2] { 15, 30 };//daño cuando acierta
    int[] hit2 = new int[2] { 0, 0 }; //daño cuando no acierta
    int[] hit3 = new int[2];//daño cuando pega doble

    public minimax()
    {
        hit3[0] = hit1[0] * 2;
        hit3[1] = hit1[1] * 2;
    }
    //para nuestro caso, la bolita aparece hijo de por medio
    public ArrayList makeTree(int depth, int IALife, int PLife, bool flagMaximizing)
    {
        if ((IALife <= 0) || (PLife <= 0))
        { //gana o pierde
            return null;
        }
        if (depth == 0)
        {
            return null;
        }
        ArrayList childrenOne = new ArrayList(); // first bolita children
        ArrayList childrenTwo = new ArrayList(); // second bolita children
        if (flagMaximizing)
        {
            string type = "min";//children of children type
            childrenOne.Add(new Node(prob1[0], makeTree(depth - 1, IALife, PLife - hit1[0], !flagMaximizing), IALife, PLife - hit1[0], hit1[0], type));
            childrenOne.Add(new Node(prob2[0], makeTree(depth - 1, IALife, PLife - hit2[0], !flagMaximizing), IALife, PLife - hit2[0], hit2[0], type));
            childrenOne.Add(new Node(prob3[0], makeTree(depth - 1, IALife, PLife - hit3[0], !flagMaximizing), IALife, PLife - hit3[0], hit3[0], type));
            childrenTwo.Add(new Node(prob1[1], makeTree(depth - 1, IALife, PLife - hit1[1], !flagMaximizing), IALife, PLife - hit1[1], hit1[1], type));
            childrenTwo.Add(new Node(prob2[1], makeTree(depth - 1, IALife, PLife - hit2[1], !flagMaximizing), IALife, PLife - hit2[1], hit2[1], type));
            childrenTwo.Add(new Node(prob3[1], makeTree(depth - 1, IALife, PLife - hit3[1], !flagMaximizing), IALife, PLife - hit3[1], hit3[1], type));
        }
        else
        {
            string type = "max"; //children of children type
            childrenOne.Add(new Node(prob1[0], makeTree(depth - 1, IALife - hit1[0], PLife, !flagMaximizing), IALife - hit1[0], PLife, hit1[0], type));
            childrenOne.Add(new Node(prob2[0], makeTree(depth - 1, IALife - hit2[0], PLife, !flagMaximizing), IALife - hit2[0], PLife, hit2[0], type));
            childrenOne.Add(new Node(prob3[0], makeTree(depth - 1, IALife - hit3[0], PLife, !flagMaximizing), IALife - hit3[0], PLife, hit3[0], type));
            childrenTwo.Add(new Node(prob1[1], makeTree(depth - 1, IALife - hit1[1], PLife, !flagMaximizing), IALife - hit1[1], PLife, hit1[1], type));
            childrenTwo.Add(new Node(prob2[1], makeTree(depth - 1, IALife - hit2[1], PLife, !flagMaximizing), IALife - hit2[1], PLife, hit2[1], type));
            childrenTwo.Add(new Node(prob3[1], makeTree(depth - 1, IALife - hit3[1], PLife, !flagMaximizing), IALife - hit3[1], PLife, hit3[1], type));

        }
        Node bolitaOne = new Node(1.0, childrenOne, IALife, PLife, 0, "bolita");
        Node bolitaTwo = new Node(1.0, childrenTwo, IALife, PLife, 0, "bolita");
        ArrayList children = new ArrayList();
        children.Add(bolitaOne);
        children.Add(bolitaTwo);
        return children;
    }

    public int heuristic(Node node)
    {
        if (node.getIALife() <= 0)
            return int.MinValue; //representacion de menos infinito
        else if (node.getPLife() <= 0)
            return int.MaxValue; //representacion de infinito
        else
        {
            int DamageMade = 100 - node.getPLife();
            int DamageGotten = 100 - node.getIALife();
            return DamageMade - DamageGotten;
        }
    }


    public double makeMinimax(Node node, int depth)
    {
        ArrayList children = node.getChildren();
        if (!node.getType().Equals("bolita") && ((depth == 0) || (children == null)))
        {
            Console.WriteLine("heuristica " + node.getIALife() + " " + node.getPLife() + " " + heuristic(node));
            return heuristic(node);
        }
        if (node.getType().Equals("bolita"))
        {
            double sum = 0;
            for (int i = 0; i < children.Count; i++)
            {
                Node child = children[i] as Node;
                sum += makeMinimax(child, depth) * child.getProbability();
            }
            Console.WriteLine("bolita " + sum);
            return sum;
        }
        else if (node.getType().Equals("max"))
        {
            double bestValue = int.MinValue; //representacion de menos infinito
            for (int i = 0; i < children.Count; i++)
            {
                Node child = children[i] as Node;
                double val = makeMinimax(child, depth - 1);
                bestValue = Math.Max(bestValue, val);
            }
            return bestValue;
        }
        else if (node.getType().Equals("min"))
        {
            double bestValue = int.MaxValue; //representacion de infinito
            for (int i = 0; i < children.Count; i++)
            {
                Node child = children[i] as Node;
                double val = makeMinimax(child, depth - 1);
                bestValue = Math.Min(bestValue, val);
            }
            return bestValue;
        }
        else return 0;
    }
}


class main
{
    public void printTree(Node node)
    {
        Console.Write(node.getIALife());
        Console.Write(" ");
        Console.Write(node.getPLife());
        Console.Write(" ");
        Console.Write(node.getType());
        Console.Write(" ... ");
        ArrayList children = node.getChildren();
        if (children != null)
        {
            for (int i = 0; i < children.Count; i++)
            {
                printTree(children[i] as Node);
            }
        }
        Console.WriteLine();
    }

    public static void Main(string[] args)
    {
        minimax obj = new minimax();
        int depth = 3;
        Node origin = new Node(1.0, obj.makeTree(depth, 30, 50, true), 30, 50, 0, "max");
        main obj_main = new main();
        obj_main.printTree(origin);
        double des = obj.makeMinimax(origin, depth);
        Console.WriteLine("minimax " + des);
        Console.ReadLine();
    }
}
