Name:		texlive-fjodor
Version:	20101026
Release:	1
Summary:	A selection of layout styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fjodor
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides several page layouts, selectable by
package options.

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
%{_texmfdistdir}/tex/latex/fjodor/fjodor.sty
%doc %{_texmfdistdir}/doc/latex/fjodor/README
%doc %{_texmfdistdir}/doc/latex/fjodor/dostojevski.pdf
%doc %{_texmfdistdir}/doc/latex/fjodor/dostojevski.tex
%doc %{_texmfdistdir}/doc/latex/fjodor/fjodor.pdf
%doc %{_texmfdistdir}/doc/latex/fjodor/fjodor.tex
%doc %{_texmfdistdir}/doc/latex/fjodor/srbook-mem.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
