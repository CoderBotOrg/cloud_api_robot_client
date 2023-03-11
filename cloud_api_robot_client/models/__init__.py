# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from cloud_api_robot_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from cloud_api_robot_client.model.activity import Activity
from cloud_api_robot_client.model.program import Program
from cloud_api_robot_client.model.robot import Robot
from cloud_api_robot_client.model.setting import Setting
