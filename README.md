# move_folders
for the monkey test, move the folders with log contains specific content to the same folder.

Such as there is a folder called `1572_crash/`, it contains many folders.
They may look like `com.example.app_xxx_Crash_xxx`, and each of them contains a log file in it, which will descripe the crash reason.

You can use this python file to move the folders that contains the same crash reason.

For example, you can change:
```
target_folder = "java.lang.ArrayIndexOutOfBoundsException"
target_string = "java.lang.ArrayIndexOutOfBoundsException"
```
to your specific crash reason, the python file will move them to the `target_folder/`.
