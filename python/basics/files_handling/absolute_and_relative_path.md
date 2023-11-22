# absolute_and_relative_path

An absolute path in Linux provides the **exact location** of a file or directory, starting from the **root directory** (/).

For example, `/home/user/documents/report.txt` is an absolute path [1](https://itslinuxfoss.com/absolute-relative-paths-linux-how-reference-them/) [2](https://linuxhandbook.com/absolute-vs-relative-path/).

A relative path in Linux refers to a file or directory **in relation to the current directory**.

For example, if you are in the `/home/user` directory and you want to access the `report.txt` file, you can use `documents/report.txt` as a relative path [1](https://itslinuxfoss.com/absolute-relative-paths-linux-how-reference-them/) [2](https://linuxhandbook.com/absolute-vs-relative-path/).

You can also use special symbols like `.` (single dot) and `..` (double dot) to refer to the current directory and the parent directory respectively [2](https://linuxhandbook.com/absolute-vs-relative-path/) [3](https://www.redhat.com/sysadmin/linux-path-absolute-relative).

For example, if you are in the `/home/user/documents` directory and you want to access the `report.txt` file, you can use `./report.txt` as a relative path. If you want to access the user directory, you can use `../` as a relative path [3](https://www.redhat.com/sysadmin/linux-path-absolute-relative).
