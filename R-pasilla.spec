%global packname  pasilla
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2.11
Release:          1
Summary:          Per-exon and per-gene read counts of RNA-seq samples of Pasilla knock-down
Group:            Sciences/Mathematics
License:          LGPL
URL:              None
Source0:          http://bioconductor.org/packages/data/experiment/src/contrib/pasilla_0.2.11.tar.gz
Requires:         R-DEXSeq R-DESeq 
Requires:         R-locfit R-edgeR R-xtable 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-DEXSeq R-DESeq
BuildRequires:    R-locfit R-edgeR R-xtable 

%description
This package provides per-exon and per-gene read counts computed for
selected genes from RNA-seq data that were presented in the article
"Conservation of an RNA regulatory map between Drosophila and mammals" by
Brooks AN, Yang L, Duff MO, Hansen KD, Park JW, Dudoit S, Brenner SE,
Graveley BR, Genome Res. 2011 Feb;21(2):193-202, Epub 2010 Oct 4, PMID:
20921232.  The experiment studied the effect of RNAi knockdown of Pasilla,
the Drosophila melanogaster ortholog of mammalian NOVA1 and NOVA2, on the
transcriptome.  The package vignette describes how the data provided here
were derived from the RNA-Seq read sequence data that is provided by NCBI
Gene Expression Omnibus under accession numbers GSM461176 to GSM461181

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
