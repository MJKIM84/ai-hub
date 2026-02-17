"use client";

import { ServiceLogo } from "./ServiceLogo";

interface ServiceDetailLogoProps {
  logoUrl: string | null;
  faviconUrl: string | null;
  ogImageUrl: string | null;
  serviceUrl: string;
  name: string;
}

export function ServiceDetailLogo(props: ServiceDetailLogoProps) {
  return <ServiceLogo {...props} size="lg" />;
}
