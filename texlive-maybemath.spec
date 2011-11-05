# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/maybemath
# catalog-date 2007-03-09 22:25:45 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-maybemath
Version:	20070309
Release:	1
Summary:	Make math bold or italic according to context
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/maybemath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maybemath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maybemath.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%{_texmfdistdir}/tex/latex/maybemath/maybemath.sty
%doc %{_texmfdistdir}/doc/latex/maybemath/README
%doc %{_texmfdistdir}/doc/latex/maybemath/maybemath.pdf
%doc %{_texmfdistdir}/doc/latex/maybemath/maybemath.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
