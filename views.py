#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render

def home(request):
    return render(request, "index.html")
