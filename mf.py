import time

cur_time_stamp = time.time()
cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")

qss_style = """
    * {
        font-size: 11px;
        font-family: "Microsoft YaHei";
    }
    QTableView {
        selection-color: #000000;
	    selection-background-color: #c4e1d2; 
    }
    QTableView::item:hover	{	
	    background-color: #a1b1c9;		
    }
"""