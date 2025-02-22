Name:		texlive-fjodor
Version:	53207
Release:	2
Summary:	A selection of layout styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fjodor
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/fjodor
%doc %{_texmfdistdir}/doc/latex/fjodor

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
