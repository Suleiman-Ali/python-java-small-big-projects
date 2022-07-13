package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        String massage = "Hello world";
        ArrayList<Integer> codedMassage = new ArrayList<>(code(massage, 1024));
        System.out.println(codedMassage);
        String decodedMassage = decode(codedMassage, 1024);
        System.out.println(decodedMassage);
        int nubmer = 'H';
        System.out.println(nubmer);


    }


    private static List<Integer> code(String massage, int plusShiftBy) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (char ch : massage.toCharArray()) {
            int myChar = ch + plusShiftBy;
            arrayList.add(myChar);
        }
        return arrayList;
    }

    private static String decode(List<Integer> codedMassage, int minusShiftBy) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int num : codedMassage) {
            char myChar = (char) (num - minusShiftBy);
            stringBuilder.append(myChar);
        }
        return stringBuilder.toString();
    }

}