<h1>Command line for the win</h1>
<h2>Bash Scripting</h2>
<p>As part of my recent project, I successfully tackled the <a href=“https://cmdchallenge.com/”>Commandline for win Challenge</a>, which involved various levels of tasks. To celebrate my accomplishment at each level,<br> I captured JPEG screenshots as evidence of my progress.</p>
<h2>Uploading Local JPEG Screenshots to a Remote Server Using SFTP:</h2>
<ol>
<li>Open your preferred command-line interface, such as Terminal (macOS), Command Prompt (Windows), or a terminal emulator (Linux).</li>
<li>Establish an SFTP connection to the remote server where you want to upload your JPEG screenshots. Replace 'username' with your actual username and 'sandbox.example.com' with the hostname or IP address of the remote server. You may need to enter your password or utilize key-based authentication, depending on the server's configuration.</li>
<li>After successfully connecting to the SFTP server, proceed to the remote server's directory where you plan to save your JPEG screenshots. If you want to upload your screenshots to a directory called 'command_line_for_the_win,' for example, use the 'cd' command to change to that directory:</li>
<li>Now, you're ready to initiate the file transfer. To upload a single JPEG screenshot, make sure you're in the directory on your local machine where the screenshot is located, or specify the full local path to the file. <br>To upload multiple files, you can utilize wildcards like * to transfer all files in your current local directory</li>
<li>Use the put * command to transfer to your remote server</li>
<li>The 'put' command will start the upload process, transferring your JPEG screenshots to the specified directory on the remote server.</li>
<li>To exit the SFTP session when you're done, type either 'exit' or 'quit':</li>
</ol>

<p>With these steps, you have successfully uploaded your local screenshot files to the remote server via SFTP. <br>They can now be accessed in the directory you specified on the remote server. <br>This process helps you securely transfer your project's progress documentation to the remote environment.
