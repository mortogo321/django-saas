import { describe, expect, it } from "vitest";

import WelcomeView from "@/views/WelcomeView.vue";
import { mount } from "@vue/test-utils";

describe("Welcome", () => {
  it("renders properly", () => {
    const wrapper = mount(WelcomeView);
    expect(wrapper.text()).toContain("Get started");
  });
});
