# Absolute and Relative Paths

## Absolute Path
An absolute path is a complete path from the root directory to the target file or directory. It always starts with the root directory (e.g., `/` in Unix/Linux systems or a drive letter like `C:` in Windows).

### Example:
- Unix/Linux: `/home/user/documents/file.txt`
- Windows: `C:\Users\User\Documents\file.txt`

## Relative Path
A relative path is a path that starts from the current working directory. It does not start with the root directory but rather from the current location in the file system.

### Example:
- If the current directory is `/home/user`:
  - `documents/file.txt` refers to `/home/user/documents/file.txt`
  - `../user2/file.txt` refers to `/home/user2/file.txt`

## Special Symbols in Relative Paths
- `.` (single dot) refers to the current directory.
- `..` (double dots) refers to the parent directory.

### Example:
- If the current directory is `/home/user/documents`:
  - `./file.txt` refers to `/home/user/documents/file.txt`
  - `../file.txt` refers to `/home/user/file.txt`
  - `../../file.txt` refers to `/home/file.txt`