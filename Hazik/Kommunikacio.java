/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package kommunikacio;

import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

/**
 *
 * @author B�lint
 */
public class Kommunikacio {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        
        System.out.println("Mit szeretn�l �rni a f�jlba?: ");
        Scanner beAkar = new Scanner(System.in);
        String beSzoveg = beAkar.nextLine();

        FileWriter beFile = new FileWriter("C:\\Users\\B�lint\\VSC Projects\\Python\\Hazik\\Doboz.txt", true);
        BufferedWriter doboz = new BufferedWriter(beFile);
        doboz.write("Java: " + beSzoveg);
        doboz.newLine();
        doboz.close();
    }

}
