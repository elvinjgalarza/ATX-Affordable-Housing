import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class csvtojson{

	private static final String path = "./data.csv";

	public static void main(String[] args) {
		System.out.println("Parsing initialized on... " + path);
		try{
			BufferedReader csvReader = new BufferedReader(new FileReader(path));
			String data[]; 
			data = new String[100];
			while (csvReader.readLine() != null) {
	    		data = csvReader.readLine().split(",");
	    		//System.out.println(csvReader.readLine());
			}

			System.out.println(data[6]);

			for(int i = 0; i < data.length; i++){
				if(data[i] == "78,705"){
					System.out.println(data[i]);
				}
			}

			csvReader.close();
		}
		catch(FileNotFoundException e){
			System.out.println("File not found at: " + path);
		}
		catch(IOException e){
			e.printStackTrace();
		}
	}

}	