# SFDX Sample "Project 2" For CumulusCI Task Test

## Summary
This is an SFDX sample repository for CumulusCI (CCI) task test.
This repository is supoosed to be used with 
[another repository](https://github.com/TamiTakamiya/sfdx-proj1).

## Setup
1. Clone this repository on your PC
1. Set your Dev Hub org with
    ```
    sfdx auth:web:login -d -a DevHub 
    ```
## Instructions
This repository contains two CCI tasks and both will complete
without errors.

1. dxtask
    ```
    cci task run dxtask
    ```
    This task should display the output of `sfdx force:org:list` command.

2. mytask
    ```
    cci task run mytask
    ```
    This task invokes the `MyTask` class defined in `scripts/tasks/MyTask.py`
    and the output message `This is my task.`