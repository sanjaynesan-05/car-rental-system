import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    private static final String URL = "jdbc:postgresql://localhost:5432/car_rental_db";
    private static final String USER = "your_username";      // Replace with your DB username
    private static final String PASSWORD = "your_password";  // Replace with your DB password

    public static Connection getConnection() {
        try {
            Class.forName("org.postgresql.Driver"); // Load PostgreSQL driver
            return DriverManager.getConnection(URL, USER, PASSWORD);
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
            return null;
        }
    }
}
