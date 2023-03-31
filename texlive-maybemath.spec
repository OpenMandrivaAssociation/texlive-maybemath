Name:		texlive-maybemath
Version:	15878
Release:	2
Summary:	Make math bold or italic according to context
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/maybemath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maybemath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maybemath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The \maybebm and \maybeit macros can be used in math
expressions to make the arguments typeset as bold or italic
respectively if the surrounding context is appropriate. They
are useful for writing user macros for use in general contexts.
\maybebm is especially appropriate when section titles contain
math expressions, since the title will appear bold but the
header and table of contents usually replicate the title in
normal width. It uses the bm package to make things bold
\maybeit performs a similar role to \mathrm{} but the math
expression will be italicised if the surrounding text is.
\maybeitsubscript is provided to shift subscripts to the left
if the expression is italicised.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/maybemath/maybemath.sty
%doc %{_texmfdistdir}/doc/latex/maybemath/README
%doc %{_texmfdistdir}/doc/latex/maybemath/maybemath.pdf
%doc %{_texmfdistdir}/doc/latex/maybemath/maybemath.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
