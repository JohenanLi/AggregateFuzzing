
# Create your tests here.
tmuxCmd = []
tmuxCmd.append("tmux new-session -s 0pdftopng -d /root/AggregateFuzzing/BackEnd/tools/memAfl/afl-fuzz  -M master -i /root/AggregateFuzzing/BackEnd/seeddir/pdf -o /root/fuzzResult/mem/pdftopng -- /root/AggregateFuzzing/BackEnd/sourceTotal/xpdf/build/xpdf/pdftopng -mono @@ o")
tmuxCmd.append("tmux new-session -s 1pdftopng -d /root/AggregateFuzzing/BackEnd/tools/memAfl/afl-fuzz  -S slave1 -i /root/AggregateFuzzing/BackEnd/seeddir/pdf -o /root/fuzzResult/mem/pdftopng -- /root/AggregateFuzzing/BackEnd/sourceTotal/xpdf/build/xpdf/pdftopng -mono @@ o")
tmuxCmd.append("tmux new-session -s 2pdftopng -d /root/AggregateFuzzing/BackEnd/tools/memAfl/afl-fuzz  -S slave2 -i /root/AggregateFuzzing/BackEnd/seeddir/pdf -o /root/fuzzResult/mem/pdftopng -- /root/AggregateFuzzing/BackEnd/sourceTotal/xpdf/build/xpdf/pdftopng -mono @@ o")
tmuxCmd.append("tmux new-session -s 3pdftopng -d /root/AggregateFuzzing/BackEnd/tools/memAfl/afl-fuzz  -S slave3 -i /root/AggregateFuzzing/BackEnd/seeddir/pdf -o /root/fuzzResult/mem/pdftopng -- /root/AggregateFuzzing/BackEnd/sourceTotal/xpdf/build/xpdf/pdftopng -mono @@ o")
tmuxCmd.append("tmux new-session -s 4pdftopng -d /root/AggregateFuzzing/BackEnd/tools/memAfl/afl-fuzz  -S slave4 -i /root/AggregateFuzzing/BackEnd/seeddir/pdf -o /root/fuzzResult/mem/pdftopng -- /root/AggregateFuzzing/BackEnd/sourceTotal/xpdf/build/xpdf/pdftopng -mono @@ o")
tmuxCmd.append("tmux new-session -s 5pdftopng -d /root/AggregateFuzzing/BackEnd/tools/memAfl/afl-fuzz  -S slave5 -i /root/AggregateFuzzing/BackEnd/seeddir/pdf -o /root/fuzzResult/mem/pdftopng -- /root/AggregateFuzzing/BackEnd/sourceTotal/xpdf/build/xpdf/pdftopng -mono @@ o")
from subprocess import run
from os import system
import libtmux
