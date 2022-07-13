package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {


        String base = matrixBuilder();
        System.out.println(base);





    }
    public static String matrixBuilder(){
        // to give random color
        Random random = new Random();

        // colors
        List<String> colors = new ArrayList<>();
        colors.add("\u001B[0m");
        colors.add("\u001B[30m");
        colors.add("\u001B[31m");
        colors.add("\u001B[32m");
        colors.add("\u001B[33m");
        colors.add("\u001B[34m");
        colors.add("\u001B[35m");
        colors.add("\u001B[36m");
        colors.add("\u001B[37m");

        // logic
        List<String> array = new ArrayList<>();
        Scanner scanner  = new Scanner(System.in);
        System.out.println("NOTE: enter 'quit' to exit.\nNOTE: use '(P)' to tell that this attribute is a key." +
                "\nNOTE: use '(FK)' to tell that this attribute is a foreign key. ");

        boolean q = false;
        while (!q) {
            System.out.println("Enter attribute name: ");
            String value = scanner.next();
            array.add(value);
            if (value.equals("quit")) {
                array.remove("quit");
                q = true;
            }
        }
        String text = "[ ";
        for (int i = 0; i < array.size(); i++){
            text += array.get(i);
            text += " | ";
        }
        text += " ]";

        // return text with random color
        return colors.get(random.nextInt(colors.size())) + text;
    }
}
