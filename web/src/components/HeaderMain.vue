<template>
    <header class="main-header">
        <div>
            <RouterLink to="/">
                <h3 class="float-md-start mb-0 text-white">KaliDocs</h3>
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