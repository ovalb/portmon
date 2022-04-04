#!/usr/bin/env python
import psutil

print("PID\tNAME\tPORT")
for proc in psutil.process_iter():
    try:
        # Just get processes associated with TTY (started from a shell)
        if proc.terminal() is not None:

            # Get the connections associated with the process
            conns = [x for x in proc.connections() if x.status == psutil.CONN_LISTEN]

            # The only times the information is valid is when the process has exactly two connections
            # and we just care about the first one
            if len(conns) == 2:
                port = conns[0].laddr.port
                print(proc.pid, "\t", proc.name(), "\t", port)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass