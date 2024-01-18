<script lang="ts">
    // import type { LayoutData } from "./$types";
    import { page } from "$app/stores";
    import Buttons from "$lib/components/Button.svelte";
    import Question from "$lib/components/Question.svelte";
    import { onNavigate } from "$app/navigation";
    import Topbar from "$lib/components/Topbar.svelte";
    import Sidebar from "$lib/components/Sidebar.svelte";

    // export let data: LayoutData;

    onNavigate(navigation => {
        //@ts-ignore
        if (!document.startViewTransition) return;

        return new Promise(resolve => {
            //@ts-ignore
            document.startViewTransition(async () => {
                resolve();
                await navigation.complete;
            });
        });
    });

    const navigations = [
        { title: "Home", path: "/home", icon: "fa-solid fa-house" },
        { title: "Settings", path: "/home/setting", icon: "fa-solid fa-gear" },
        { title: "Quest", path: "/home/quest", icon: "fa-solid fa-scroll" },
        { title: "Leaderboard", path: "/home/leaderboard", icon: "fa-solid fa-trophy" }
    ];
</script>

<main class="--bg-neutral-100">
    <Topbar />
    <Sidebar {navigations} pageUrlPathname={$page.url.pathname}>
        <slot />
    </Sidebar>
</main>
