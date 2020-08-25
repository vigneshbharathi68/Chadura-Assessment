# Task 1. What is Linux?
Just like Windows, iOS, and Mac OS, Linux is an operating system. In fact, one of the most popular platforms on the planet, Android, is powered by the Linux operating system. An operating system is software that manages all of the hardware resources associated with your desktop or laptop.To put it simply, the operating system manages the communication between your software and your hardware. Without the operating system (OS), the software wouldn?t function.
**Linux is also distributed under an open source license. Open source follows these key tenants:**
- The freedom to run the program, for any purpose.
- The freedom to study how the program works, and change it to make it do what you wish.
- The freedom to redistribute copies so you can help your neighbor.
- The freedom to distribute copies of your modified versions to others.

Linux has a number of different versions to suit any type of user. From new users to hard-core users, you’ll find a “flavor” of Linux to match your needs. These versions are called distributions (or, in the short form, “distros”). Nearly every distribution of Linux can be downloaded for free, burned onto disk (or USB thumb drive), and installed (on as many machines as you like).
**Popular Linux distributions include:**
- Linux Mint
- Debian
- Ubuntu
- Antergos
- Solus

# Task 2. Define Linux kernel?
- The Linux kernel, developed by contributors worldwide, is a free and open-source, monolithic, modular (i.e., it supports the insertion and removal at runtime of loadable kernel objects), Unix-like operating system kernel.

- It is deployed on a wide variety of computing systems, such as embedded devices, mobile devices (including its use in the Android operating system), personal computers, servers, mainframes, and supercomputers.

- The Linux kernel was conceived and created in 1991 by Linus Torvalds for his personal computer and with no cross-platform intentions, but has since ported to a wide range of computer architectures. Notwithstanding this, the Linux kernel is highly optimized with the use of architecture specific instructions (ISA), therefore portability isn't as easy as it is with other kernels (e.g., with NetBSD, that as of 2019 supports 59 hardware platforms).

- Linux was soon adopted as the kernel for the GNU Operating System, which was created as an open source and free software, and based on UNIX as a by-product of the fallout of the Unix wars. Since then it has spawned a plethora of operating system distributions, commonly also called Linux, although, formally, the term "Linux" refers only to the kernel.

# Task 3.  What is the difference between 32bit and 64bit computers? How much maximum memory access they can have?
- Simply put, a ***64-bit processor is more capable than a 32-bit processor, because it can handle more data at once***. A 64-bit processor is capable of storing more computational values, including memory addresses, which means it’s able to access over four billion times the physical memory of a 32-bit processor. That’s just as big as it sounds
- Here’s the key difference: 32-bit processors are perfectly capable of handling a limited amount of RAM **(in Windows, 4GB or less)**, and 64-bit processors are capable of utilizing much more.
# Task 4. What is git and what version is installed on your Linux machine?
Git is a distributed version control system, meaning your local copy of code is a complete version control repository. These fully-functional local repositories make it is easy to work offline or remotely. You commit your work locally, and then sync your copy of the repository with the copy on the server. This paradigm differs from centralized version control where clients must synchronize code with a server before creating new versions of code.

Every time you save your work, Git creates a commit. A commit is a snapshot of all your files at a point in time. If a file has not changed from one commit to the next, Git uses the previously stored file. This design differs from other systems which store an initial version of a file and keep a record of deltas over time.

## Branches

Each developer saves changes their own local code repository. As a result, you can have many different changes based off the same commit. Git provides tools for isolating changes and later merging them back together. Branches, which are lightweight pointers to work in progress, manage this separation. Once your work created in a branch is finished, merge it back into your team’s main (or master) branch.

### Benefits of Git

**Simultaneous development**

Everyone has their own local copy of code and can work simultaneously on their own branches. Git works when you’re offline since almost every operation is local.

**Faster releases

Branches allow for flexible and simultaneous development. The main branch contains stable, high-quality code from which you release. Feature branches contain work in progress, which you merge into the main branch upon completion. By separating your release branch from development in progress, you can manage your stable code better and ship updates more quickly.

**Built-in integration

Due to its popularity, Git is integrated into most tools and products. Every major IDE has built-in Git support, and many tools that allow you to manage continuous integration, continuous deployment, automated testing, work item tracking, metrics, and reporting feature integration with Git. This integration simplifies your day to day workflow.

**Strong community support

Git is open-source and has become the de facto standard for version control, and there is no shortage of tools and resources available for your team to leverage. The volume of community support for Git compared to other version control systems makes it easy to get help when you need it.

**Git works with team

Using Git with a source code management tool can increase your team’s productivity by encouraging collaboration, enforcing policies, automating processes, and improving visibility and traceability of work. You may choose individual tools for version control, work item tracking, and continuous integration and deployment.

Use pull requests to discuss code changes with your team before merging them into your main branch. The discussions you have in pull requests are invaluable to ensuring code quality and increase knowledge across your team. Visual Studio Team Services offers a rich pull request experience where you can browse file changes, leave comments, inspect commits, view builds, and vote to approve the code.
