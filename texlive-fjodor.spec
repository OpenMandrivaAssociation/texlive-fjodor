# revision 20220
# category Package
# catalog-ctan /macros/latex/contrib/fjodor
# catalog-date 2010-10-26 21:52:03 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-fjodor
Version:	20101026
Release:	4
Summary:	A selection of layout styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fjodor
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides several page layouts, selectable by
package options.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101026-2
+ Revision: 751917
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101026-1
+ Revision: 718454
- texlive-fjodor
- texlive-fjodor
- texlive-fjodor
- texlive-fjodor

