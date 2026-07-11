%global tl_name edfnotes
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6b
Release:	%{tl_revision}.1
Summary:	Critical annotations to footnotes with ednotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/edfnotes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edfnotes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package modifies the annotation commands and label-test mechanism of
the ednotes package so that critical notes appear on the pages and in
the order that one would expect.

