Name:		texlive-edfnotes
Version:	21540
Release:	2
Summary:	Critical annotations to footnotes with ednotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/edfnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package modifies the annotation commands and label-test
mechanism of the ednotes package so that critical notes appear
on the pages and in the order that one would expect.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
