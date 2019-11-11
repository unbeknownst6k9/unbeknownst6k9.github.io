void GetPeep(Block *p_block) {
	int print = 0;
	Block* ref = p_block
	while (p_block != NULL) {
		print = 1;
		printf("the position is %d\n", ref->ledger[i].position);
		printf("the character is %c\n", ref->ledger[i].character);
		if (ref->ledger[i].event_type)
		{
			printf("add to the peep\n");
		}
		else
		{
			printf("remove from the peep\n");
		}
		ref = ref->next;
		
	}
	if (!print) {
		printf("the blockchain is empty\n");
	}
}


void GetPeepAtTime(Block *p_block, unsigned long times) {
	int print = 0, i = 0;
	/*p_block begins with genesis block and this should be skipped*/
	Block* ref = p_block->next;
	while (ref != NULL)
	{
		print = 1;
		while (ref->ledger[i].timestamp && i< 64)
		{
			printf("the position is %d\n", ref->ledger[i].position);
			printf("the character is %c\n", ref->ledger[i].character);
			if (ref->ledger[i].event_type)
			{
				printf("add to the peep\n");
			}
			else
			{
				printf("remove from the peep\n");
			}
			i++;
		}
		ref = ref->next;
	}
	if (!print)
	{
		printf("the timestamp is before the blockchain or the blockchain is empty\n");
	}
}