# Project Hand-in Procedure

  * Create a repository on Github, which includes everything, the code of your project, all related artifacts, etc.
  * Create a Markdown (.md) file called README.md in the root of your project.
  * That README.md describes what this project does, how it works, how it is setup, etc.
  * Create a release of your project on Github, see https://help.github.com/articles/creating-releases/.
  * Hand-in a link to this release on Moodle. Latest hand-in is on 3. Jun. 12:00 (noon).


# Getting Things Done with Python

Repository containing the course material for the elective course "Getting Things Done with Python" (Spring 2018) at CPH Business Academy (www.cphbusiness.dk).


# Your Easter Egg!

The first two members of this course that find the easter egg will get a Python book!

![](lecture_notes/images/commander_keen_easteregg.png)


# Organisational Notes

Find a detailed description of the plan and the curriculum for the semester here:

  * Dates: https://datsoftlyngby.github.io/dat4sem2018spring/
  * Plan: https://datsoftlyngby.github.io/dat4sem2018spring/Python_plan.html


## I want to work with the notebooks, but do not have a Jupyter environment.

The easiest way to work with the notebooks in this repository is to run it in a container on [MyBinder](https://mybinder.org).

**Click here:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/datsoftlyngby/dat4sem2018spring-python/master) to start an interactive environment.


## I want to work with the course material on my machine.

Best fork this repository on Github.

And fetch the latest changes before/after each lecture, see https://help.github.com/articles/syncing-a-fork/.






## I do not have a Linux installed, but some of your stuff uses Bash scripts?!?

In the following is a step by step guide to get you up and running with Vagrant and VirtualBox to run an Ubuntu Linux to run the code examples presented in class.

This guide is written for Windows Users.


### Required Software

  * VirtualBox
  * Vagrant
  * GitBash


### Step-by-step Installation Guide

  * Download URL: https://git-scm.com/download
    - During installation choose the following:
      * _Use Git from the Windows Command Prompt_ with this option you will be able to use Git from both Git Bash and the Windows Command Prompt.
      * _Checkout as-is, commit Unix-style line endings_
  * Download and install VirtualBox (https://www.virtualbox.org/wiki/Downloads)
    - The current version is 5.2.6
      * Get it from here: [http://download.virtualbox.org/virtualbox/5.2.6/VirtualBox-5.2.6-120293-Win.exe](http://download.virtualbox.org/virtualbox/5.2.6/VirtualBox-5.2.6-120293-Win.exe)
      * Download the extension pack too: [http://download.virtualbox.org/virtualbox/5.2.6/Oracle_VM_VirtualBox_Extension_Pack-5.2.6.vbox-extpack](http://download.virtualbox.org/virtualbox/5.2.6/Oracle_VM_VirtualBox_Extension_Pack-5.2.6.vbox-extpack)
      * After installing VirtualBox, open it and click `File` -> `Preferences` -> `Extensions` and click the marked icon
      ![](https://www.swtestacademy.com/wp-content/uploads/2017/04/img_58e13f8fc72fe.png)
      * Select the downloaded extension pack and then click `Install` -> `I Agree` -> `Yes`
  * Download and install Vagrant (https://www.vagrantup.com/downloads.html)
  * Adapt the computer's settings:
    - **Enable VT-X** (Intel Virtualization Technology) in your computer BIOS/UEFI. (**OBS** You enter your BIOS after restarting the computer and hit a key like `F1`, `F2`, up to `F12` or `DELETE`. Which button to press depends on the vendor and the model of you computer. Find that in your computer's manual.)
    - **Disable Hyper-V** on program and features page in the control panel.
      ![](https://camo.githubusercontent.com/99700ca628f407bb3f3a7201f7e00bbfccae107a/687474703a2f2f692e696d6775722e636f6d2f5a6a50324b49432e706e67)
  * If you did not already generate an SSH keypair, generate one (e.g., via `ssh-keygen -t rsa` in GitBash)

  * Now everything is installed. See if you can run `vagrant --version` in GitBash.


### Creating a virtual machine for the Database class

A virtual machine (VM) is created from a `Vagrantfile`. Get the one for the course from the root of the course's repository [https://github.com/datsoftlyngby/dat4sem2018spring-python](https://github.com/datsoftlyngby/dat4sem2018spring-python).

Likely it is best to fork this repository on GitHub (`Fork` button on the top right of the page). This will create a fork of the repository for your GitHub user. In the following your GitHub user is designated as `<yourghuser>`. You have to replace it with your ID before pasting the corresponding commands. All of the following commands have to be run in GitBash.


  * Clone the repository:
  ```bash
  $ git clone git@github.com:<yourghuser>/dat4sem2018spring-python.git
  ```
  * **Hint** In case you want to modify the configuration of the virtual machine, which will be created, you can do this now. Edit it with an editor of your choice. For example, to give the VM more RAM adapt the line `vb.memory = "3072"` to a value of RAM in megabyte, which fits your host machine.
  * Start-up the VM:
  ```bash
  $ cd dat4sem2018spring-python
  $ vagrant up
  ```
  * The first time you run the `vagrant up` command it will take a bit as it has to download the corresponding Ubuntu Linux image and intall the required software on it. **OBS** to run this step, you have to be connected to the internet. Do not interrupt the process and keep track that no errors 
  * To log onto the virtual machine after completion of `vagrant up` execute:
  ```bash
  vagrant ssh
  ```
  * Now, you should be logged onto the VM and you should see a Bash prompt similar to:
  ```bash
  vagrant@vagrant:~$
  ```
  * Python is installed and configured on the VM. Test it via:
  ```bash
  vagrant@vagrant:~$ python --version
  Python 3.6.3 :: Anaconda custom (64-bit)
  ```
  * You can start the Jupyter notebook server via:
  ```bash
  vagrant@vagrant:~$ notebook
  ```
  * When you are done working on your VM, you can leave it by issuing the exit command.
  ```bash
  vagrant@vagrant:~$ exit
  ```
  * Subsequently, you can put the VM to "sleep" (just like closing the lid of your notebook) by running vagrant suspend on your host machine.
  ```bash
  $ vagrant suspend
  ```

  * In case you want to discard this VM just run `vagrant destroy` from within the directory containing the `Vagrantfile`. 



## References

This guide is adapted from earlier versions and from https://www.swtestacademy.com/quick-start-vagrant-windows-10/


-------------------
