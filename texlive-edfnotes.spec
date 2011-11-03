# revision 21540
# category Package
# catalog-ctan /macros/latex/contrib/edfnotes
# catalog-date 2011-02-22 21:47:43 +0100
# catalog-license lppl1.3
# catalog-version 0.6b
Name:		texlive-edfnotes
Version:	0.6b
Release:	1
Summary:	Critical annotations to footnotes with ednotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/edfnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package modifies the annotation commands and label-test
mechanism of the ednotes package so that critical notes appear
on the pages and in the order that one would expect.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/edfnotes/edfnotes.sty
%doc %{_texmfdistdir}/doc/latex/edfnotes/PdUsample.pdf
%doc %{_texmfdistdir}/doc/latex/edfnotes/README
%doc %{_texmfdistdir}/doc/latex/edfnotes/README.pdf
%doc %{_texmfdistdir}/doc/latex/edfnotes/README.txt
%doc %{_texmfdistdir}/doc/latex/edfnotes/SRCFILEs.txt
%doc %{_texmfdistdir}/doc/latex/edfnotes/edfnotes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/edfnotes/README.tex
%doc %{_texmfdistdir}/source/latex/edfnotes/edfnotes.tex
%doc %{_texmfdistdir}/source/latex/edfnotes/srcfiles.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
