package com;


import java.io.IOException;
import java.io.PrintWriter;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class SuccessServlet extends HttpServlet {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String message;
	
	public void init() throws ServletException {
		 // Do required initialization
		 message = "Memory Test Success";
	}
	   
	//This function does the Get operation:
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//Get Request URL	
	    
		StringBuffer requestURL = request.getRequestURL();
		int memory = 0;
		
		Map<String, String[]> paramsMap = request.getParameterMap();
		for (String key : paramsMap.keySet()) {
		    System.out.println("Key  " + key);

			if (key.equals("memorysize")) {
			   String string_memory  = request.getParameter(key);
			   memory = Integer.parseInt(string_memory);
			   }
			if (key.equals("oome")) {
					try {
						generateOOM();
					} catch (Exception e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			if (key.equals("max")) { 
				//Max Memory:
				System.out.println(Runtime.getRuntime().maxMemory());
			}
		}
		
	    System.out.println("The default memory is " + memory);
	      
	    // Set response content type
	    response.setContentType("text/html");

	    // Actual logic goes here.
	    PrintWriter out = response.getWriter();
	    out.println("<h1>" + message + "</h1>");
	   

	}
	
	/*Original function - which works returning Hello, Mike*/
	public void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {

        PrintWriter out = res.getWriter();
        out.write("Hello , Mike");
        out.close();
    }
	
	/*Generate OOME*/
	public void generateOOM() throws Exception {
		int iteratorValue = 20;
		System.out.println("\n=================> OOM test started..\n");
		for (int outerIterator = 1; outerIterator < 20; outerIterator++) {
			System.out.println("Iteration " + outerIterator + " Free Mem: " + Runtime.getRuntime().freeMemory());
			int loop1 = 2;
			int[] memoryFillIntVar = new int[iteratorValue];
			// feel memoryFillIntVar array in loop..
			do {
				memoryFillIntVar[loop1] = 0;
				loop1--;
			} while (loop1 > 0);
			iteratorValue = iteratorValue * 5;
			System.out.println("\nRequired Memory for next loop: " + iteratorValue);
			Thread.sleep(1000);
		}
	}
	/*Destroy*/
	public void destroy() {
		      // do nothing.
	}
	
}
