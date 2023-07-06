const getInstallationSettings = async ({ confirm }) => {
    const settings = {
        data: {
            code_ownership: false,
            api_gateway_enabled: false,
            rds: false,
            sonar_cloud: false,
            onboarding: false
        },
    } as any;

    settings.data.code_ownership = await confirm(
      'If you wish to have CODEOWNER level control on this service, please ensure to add your respective team name from gitlab when you are asked for your \\"team\\" name. You can find your team name at https://gitlab.com/sennder/code-owners',
      false
    )
    
    settings.data.onboarding = await confirm(
      'Do you want to deploy this service for an onboarding process?',
      false
    )

    settings.data.api_gateway_enabled = await confirm(
      'Do you want external routing via an API gateway. It can be added later.',
      false
    )

    settings.data.rds = await confirm(
      'Do you want a postgres database. It can be added later.',
      false
    )

    settings.data.sonar_cloud = await confirm(
      'Do you want a SonarCloud CI job in your pipeline.\\n\u001b[33mCheck https://gitlab.com/sennder/cross-cutting/senn-node/ts-templates/-/tree/main/k8s-fastapi-app#sonarcloud-integration for how to fully activate it!\\nOtherwise the SonarCloud job will fail.\u001b[0m',
      false
    )

    return settings;
};

module.exports = {
    getInstallationSettings
}
