STAN_TIME = 8 
OVER_TIME = 11


class Operation:
	def __init__(self, index, optype, oplength):
		self.i = index
		self.t = optype
		self.l = oplength

class Room:
	def __init__(self, index):
		self.index = index
		self.oplist = []
		self.optypelist = [0] * 10
		self.totaltime = 0
		self.overwork = False

def printroomlist(roomlist):
	for i in range(12):
		print("Room index: {}".format(i))
		print("Operation order: {}".format(roomlist[i].oplist))
		print("Operation type sum: {}".format(sum(roomlist[i].optypelist)))
		print("Total work time: {} hours".format(roomlist[i].totaltime))
		print("Over work: {}".format(roomlist[i].overwork))
		print()

oplist1 = [Operation(0, 1, 1.75), Operation(1, 1, 1.5), Operation(2, 6, 3.5), Operation(3, 6, 3), Operation(4, 6, 3),
	Operation(5, 6, 2.42), Operation(6, 6, 6), Operation(7, 6, 2), Operation(8, 6, 3.5), Operation(9, 6, 2.75),
	Operation(10, 4, 2.75), Operation(11, 4, 1.83), Operation(12, 4, 5.25), Operation(13, 4, 2.75), Operation(14, 4, 2.75), 
	Operation(15, 4, 1.83), Operation(16, 4, 3.25), Operation(17, 4, 1.83), Operation(18, 5, 4.42), Operation(19, 5, 3), 
	Operation(20, 5, 3.17), Operation(21, 5, 4.25), Operation(22, 5, 4.33), Operation(23, 5, 3.67), Operation(24, 5, 2.92), 
	Operation(25, 5, 2.17), Operation(26, 5, 3.33), Operation(27, 5, 2), Operation(28, 3, 0.67), Operation(29, 7, 4.08), 
	Operation(30, 7, 2.25), Operation(31, 7, 2.25), Operation(32, 8, 5.25), Operation(33, 8, 6), Operation(34, 8, 6),
	Operation(35, 8, 5.5), Operation(36, 8, 4.75), Operation(37, 9, 5)]
oplist1_sorted = sorted(oplist1, key=lambda item:item.l, reverse=True)
oplist1_sorted_index = [item.i for item in oplist1_sorted]

roomlist1 = [Room(0), Room(1), Room(2), Room(3), Room(4), Room(5), Room(6), Room(7), Room(8), Room(9), Room(10), Room(11)]
roomlist1_sorted = sorted(roomlist1, key=lambda item:item.totaltime)
roomlist1_sorted_index = [item.index for item in roomlist1_sorted]

for i in oplist1_sorted_index:
	strat_index = 0
	roomlist1[roomlist1_sorted_index[strat_index]].oplist.append(i)
	roomlist1[roomlist1_sorted_index[strat_index]].totaltime += oplist1[i].l
	roomlist1[roomlist1_sorted_index[strat_index]].optypelist[oplist1[i].t] = 1
	if roomlist1_sorted[strat_index].totaltime > STAN_TIME:
		roomlist1_sorted[strat_index].overwork = True

	roomlist1_sorted = sorted(roomlist1, key=lambda item:item.totaltime)
	roomlist1_sorted_index = [item.index for item in roomlist1_sorted]	

printroomlist(roomlist1)
# print([oplist1[i].l for i in oplist1_sorted_index])