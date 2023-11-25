# Maxinne-RealTimeChatAPP

 To create a simple real-time chat-app using python sockets + Tkinter + Threading:

In Server:
1.Import Necessary Modules:
	Import the ‘socket’ and ‘threading’ modules at the beginning of your code.

2.Define the ‘handle_client’ Function:
  This function is responsible for handling individual client connections. It takes two parameters:’client_socket’ and ‘client_address’.
  Inside the function, it continuously receives messages from the client using a while loop.
  If the client sends an empty message, it breaks out of the loop and closes the connection.
  The received message is then printed, and the ‘broadcast’ function is called to send the message to all connected clients except the sender.
  If an ‘OSError’ occurs (e.g., the client disconnects), it breaks out of the loop, closes the connection, and removes the client socket from the list.

3.Define the ‘broadcast’ Function:
  This function sends a message to all connected clients except the sender.
  It iterates through the list of  ‘client_sockets’  and sends the message using ‘send()’.
  If a ‘socket.error’ occurs (e.g., a client disconnects), it removes the problematic client socket from the list.

4.Configure the server:
  Set the ‘HOST’ and ‘PORT’ variables to define the server's IP address and port number.
  Create a new’ socket’ object (‘server_socket’) using ‘socket.AF_INET’ for IPv4 and ‘.SOCK_STREAM’ for TCP.
  Bind the server socket to the specified host and port.
  Listen for incoming connections with a backlog of 5.

5.Initialize a List for Connected Clients:
  Create an empty list called ‘client_sockets’ to keep track of connected clients.

6.Accept and Handle Incoming Connections:
  Start an infinite loop to accept incoming connections.
  When a client connects, accept the connection (‘server_socket.accept()’), add the client socket to the list, and start a new thread (‘client_thread’) to handle the client using the ‘handle_client’ function.

7.Run the server:
  Print a message indicating that the server is listening on a specific host and port.

8.Run the Server in the Main Thread:
  The server runs in the main thread, continuously accepting new connections and       
    creating threads to handle them.
    
To run the server, execute the script, and it will start listening for incoming connections. Each connected client will be handled in a separate thread.



In Client:
1. Import Necessary Modules:
  Import the required modules, including tkinter, messagebox, socket, and threading.

2. Define the receive_messages Function:
  This function runs in a separate thread and continuously receives messages from the server.
  It decodes the received message and inserts it into the Tkinter Listbox (message_listbox).

3. Define the send_message Function:
  This function is called when the user sends a message either by pressing the "Send" button or pressing the Enter key in the entry field.
  It retrieves the user's message from the entry field, sends it to the server using the client socket, and inserts the message into the local Listbox.

4. Define the on_closing Function:
  This function is called when the user closes the application window.
  It closes the client socket and destroys the Tkinter window.

5. Create the Tkinter Window:
  Create the main Tkinter window (root) with the title "CHAT APP."

6. Create the Message Listbox:
  Create a Tkinter Listbox (message_listbox) to display received and sent messages.
  Attach a scrollbar to the Listbox to handle scrolling.

7. Create the Entry Field:
  Create an entry widget (entry_field) for user input.
  Bind the <Return> key to the send_message function so that pressing Enter sends the message.

8. Create the Send Button:
  Create a Tkinter Button (send_button) labeled "Send" that calls the send_message function when clicked.

9. Set Up the Socket Connection:
  Set the server's IP address (HOST) and port number (PORT).
  Create a client socket (client_socket) and connect it to the server.

10. Start the Receive Thread:
  Start a separate thread (receive_thread) to continuously receive messages from the server.

11. Configure the Closing Event:
  Configure the closing event to call the on_closing function when the user closes the window.

12. Start the Tkinter Event Loop:
  Start the Tkinter event loop (root.mainloop()) to run the GUI application.

To run the client, execute the script, and a Tkinter window will appear. Enter the server's IP address and port, and you should be able to send and receive messages in the chat application. 
