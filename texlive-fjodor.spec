%global tl_name fjodor
%global tl_revision 53207

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A selection of layout styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fjodor
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fjodor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides several page layouts, selectable by package
options.

