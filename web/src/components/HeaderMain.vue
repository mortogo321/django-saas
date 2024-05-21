<template>
    <header class="main-header w-full">
        <div class="py-3">
            <RouterLink to="/" class="navbar-brand">
                <h3 class="float-md-start mb-0">KaliDocs</h3>
            </RouterLink>

            <nav class="nav nav-masthead justify-content-center float-md-end">
                <RouterLink
                    to="/"
                    class="nav-link fw-bold py-1 px-0"
                    activeClass="active"
                    aria-current="page">
                    Home
                </RouterLink>
                <RouterLink
                    to="/about"
                    class="nav-link fw-bold py-1 px-0"
                    activeClass="active"
                    aria-current="page">
                    About
                </RouterLink>
            </nav>
        </div>
    </header>
</template>