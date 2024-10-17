Name:		texlive-mindflow
Version:	65236
Release:	1
Summary:	Write your ideas in a clear way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mindflow
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mindflow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mindflow.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mindflow.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an environment that has its own line
numbers or markers and can be well distinguished from the main
text, for writing your ideas or annotations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mindflow
%{_texmfdistdir}/tex/latex/mindflow
%doc %{_texmfdistdir}/doc/latex/mindflow

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
