#!/bin/bash

touch $1
chmod 744 $1
echo "#!/usr/bin/env python3" >> $1