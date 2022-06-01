void plot_var(){
	//TMultiGraph *mg=new TMultiGraph();
	gStyle->SetOptStat(kFALSE);
	string fileNames[]={"pp_ttbar.root","pp_ttbar_nlo.root"};
	TString legend[]={"LO","NLO"};

	TString vars[]={"top_pt","top_eta","antitop_pt","antitop_eta","delta_eta","M_tt","delta_rapidity"};
	TString xaxisNames[]={"p_{T}(GeV)","#eta","p_{T}(GeV)","#eta","#Delta#eta_{tt}","M_{t#bar{t}}(GeV)","#Deltay_{t#bar{t}}"};

	for(int i=0;i<7;i++){ 		//loop over variables
		TCanvas *c2=new TCanvas();
		auto leg=new TLegend(.7,.7,.9,.9);
		for(int j=0;j<2;j++){ 		//loop over files
			TFile *file=TFile::Open(fileNames[j].c_str());
			TH1F *hist=(TH1F*) file->Get(vars[i]);
			Double_t scale=1/hist->Integral();
			hist->Scale(scale);
			if(j==0){                                                  
				hist->Draw("hist");
				hist->GetXaxis()->SetTitle(xaxisNames[i]);
				hist->GetYaxis()->SetTitle("Probability");
				hist->GetYaxis()->SetRangeUser(0,(hist->GetMaximum())*1.4);

				
				hist->GetXaxis()->SetLabelFont(42);
				hist->GetXaxis()->SetLabelOffset(0.007);
				hist->GetXaxis()->SetLabelSize(0.04);
				hist->GetXaxis()->SetTitleSize(0.06);
				hist->GetXaxis()->SetTitleOffset(0.9);
				hist->GetXaxis()->SetTitleFont(42);

				hist->GetYaxis()->SetLabelFont(42);
				hist->GetYaxis()->SetLabelOffset(0.007);
				hist->GetYaxis()->SetLabelSize(0.04);
				hist->GetYaxis()->SetTitleSize(0.06);
				hist->GetYaxis()->SetTitleOffset(1.1);
				hist->GetYaxis()->SetTitleFont(42);

				hist->GetXaxis()->CenterTitle();
				hist->GetYaxis()->CenterTitle();
				hist->SetTitle("");
			}
			else
				hist->Draw("samehist");

			TLegendEntry *leg_entry=leg->AddEntry(hist,legend[j]);
			if(j<3){
				hist->SetLineColor(j+2);
				leg_entry->SetTextColor(j+2);
				}
			else{ 
				hist->SetLineColor(6);
			    leg_entry->SetTextColor(6); 
			    }
			hist->SetLineWidth(2);
		}
		
		c2->SetLeftMargin(0.15);
		c2->SetRightMargin(0.10);
		c2->SetTopMargin(0.07);
		c2->SetBottomMargin(0.13);
		leg->DrawClone("same");
		gPad->SetGrid();
		gPad->Print(vars[i]+".png");
	}
}