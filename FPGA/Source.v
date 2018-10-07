module DFF(output Q, Q_BAR,
	   input D, CLK);
	reg Q, Q_BAR;
	wire D, CLK;

	nand U1 (X, D, CLK);
	nand U2 (Y, X, CLK);
	nand U3 (Q, Q_BAR, X);
	nand U4 (Q_BAR, Q, Y); 
endmodule

module testBench();
	reg Q, Q_BAR;
	wire D, CLK;

	DFF dff1 (.Q(Q), .Q_BAR(Q_BAR), .D(D), .CLK(CLK));

	always #2 CLK = ~CLK;
endmodule
