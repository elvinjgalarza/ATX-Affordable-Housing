import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

class csvtojson{

	private static final String path = "./data.csv";

	public static void main(String[] args) {
		System.out.println("Hello");
		try{
			BufferedReader csvReader = new BufferedReader(new FileReader(path));
			while (csvReader.readLine() != null) {
    			String[] data = csvReader.readLine().split(",");
    			System.out.println(data[1]);
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